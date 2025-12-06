# System Architecture Summary

## Backend
- FastAPI (see `backend/app/main.py`) exposes a single FastAPI instance with CORS and a health endpoint; `backend/app/core/config.py` centralizes settings such as JWT secrets, database URL, and prefixes while `backend/app/db/session.py` wires SQLAlchemy to `SessionLocal` backed by that config.
- Business entities live under `backend/app/db/models/` (Users, Items, PurchaseBatch, Sale, Expense, Investment, Document, GSTLedger) with relationships wired to `Base` from `backend/app/db/base.py`. Schemas under `backend/app/schemas/` describe the expected request/response shapes, and `backend/app/api/v1/routes/` is where each domain (items, purchases, sales, expenses, investments, analytics, GST, documents, auth, reports) will expose FastAPI routers.
- The remaining backend pillars are service layers (`backend/app/services/`) that will implement FIFO/GST/profit/document logic, and the factory packages (`backend/app/factories/`) that will eventually provide concrete engines for inventory, GST, profit, and storage adapters.

## Frontend
- A Next.js 14 App Router application lives under `frontend/app/` with entry pages for login, dashboard, items, purchases, sales, expenses, investments, documents, and analytics. `frontend/app/layout.tsx` and `globals.css` share layout and styling decisions, while `middleware.ts` is the hook point for auth enforcement.
- Shared UI bits live in `frontend/components/` (Navbar, Sidebar, Card, Chart, Loader) and `frontend/utils/helpers.ts` (utility functions). `frontend/services/` is the planned API surface (e.g., `apiClient.ts`, `authService.ts`, `analyticsService.ts`) and `frontend/hooks/` (e.g., `useAuth.ts`, `useApi.ts`) will coordinate stored tokens / data fetching scaffolding.
- The frontend talks to `http://localhost:8000` by default (`frontend/services/apiClient.ts`) and will consume the REST endpoints described in `docs/api_spec.md`.

# Module Breakdown

## Backend Modules
- **API Routes (`backend/app/api/v1/routes/`)** – each resource (auth, items, purchases, sales, expenses, investments, analytics, GST, documents, reports) will get its own `APIRouter` which marshals `Pydantic` schemas and delegates to services.
- **Schemas (`backend/app/schemas/`)** – define the request payloads, response DTOs, and shared primitives (tokens, analytics summaries, documents).
- **Database (`backend/app/db/`)** – SQLAlchemy models, `SessionLocal`, and Alembic registration (`base.py`) provide persistence for every domain object.
- **Services (`backend/app/services/`)** – implement the core business logic (inventory FIFO `fifo_service`, GST ledger `gst_service`, profit computation `profit_service`, document handling `document_service`, etc.).
- **Factories (`backend/app/factories/`)** – encapsulate interchangeable business engines (inventory, GST, profit, storage) so the services can stay decoupled from concrete implementations.

## Frontend Modules
- **App Pages (`frontend/app/…/page.tsx`)** – each feature (dashboard, purchases, sales, expenses, investments, documents, analytics, login) is a route that renders shared components and pulls in services/hooks.
- **Components (`frontend/components/`)** – reusable UI primitives for navigation (`Navbar`, `Sidebar`), loading states (`Loader`), data presentation (`Card`, `Chart`).
- **Services (`frontend/services/`)** – wrapper around fetch (`apiClient.ts`) plus domain-specific helpers that can be filled out (`authService`, `itemsService`, `purchaseService`, `analyticsService`, etc.).
- **Hooks/Utils (`frontend/hooks/`, `frontend/utils/helpers.ts`)** – stateful helpers (`useAuth`, `useApi`) and helpers to keep the UI/UX consistent.

# Development Roadmap

- **Phase A – API Foundation**
  - Epic: Backend CRUD infrastructure
    - User Story: As a backend developer, I want item CRUD scaffolding so the API can persist catalog data.
      - Tasks:
        - Define `ItemUpdate` in `backend/app/schemas/item_schema.py` so updates stay typed while reusing existing DTOs.
        - Implement `backend/app/services/item_service.py` with `create_item`, `get_item`, and `list_items` functions that open a session, call the `Item` model, and return ORM objects.
        - Build `backend/app/api/v1/routes/items.py` to mount a `router = APIRouter(prefix="/items")` exposing `POST /items/` and `GET /items/` using the new service and schemas.
    - User Story: As a backend developer, I need purchases to create FIFO batches so stock tracking begins.
      - Tasks:
        - Expand `backend/app/schemas/purchase_schema.py` with `PurchaseCreate` and `PurchaseRead` models covering `item_id`, `quantity`, `rate`, `gst_percent`, `invoice_number`, and timestamps.
        - Add `backend/app/services/purchase_service.py` with `create_purchase_batch` that persists `PurchaseBatch` and `list_purchase_batches` that returns recent entries.
        - Wire `backend/app/api/v1/routes/purchases.py` to accept POST payloads, call the service, and emit the `PurchaseRead` response.
    - User Story: As a backend developer, I need sales creation to exercise FIFO deductions via a simple endpoint.
      - Tasks:
        - Add `SaleCreate`/`SaleRead` models inside `backend/app/schemas/sale_schema.py` describing sell quantity, rate, GST, COGS, and remaining stock.
        - Implement `backend/app/services/sale_service.py` with `create_sale` stub that records a `Sale`.
        - Implement `backend/app/api/v1/routes/sales.py` with POST/GET handlers hooked to the service.

- **Phase B – Business Logic & Analytics**
  - Epic: FIFO + GST engines
    - User Story: As the accounting engine, I want FIFO deduction logic to compute COGS for every sale.
      - Tasks:
        - Implement `backend/app/services/fifo_service.py` logic to fetch oldest `PurchaseBatch` rows, subtract quantities, and return consumed batches.
        - Persist COGS results inside `Sale` records during `create_sale`.
        - Create `backend/app/factories/inventory_factory.py` that exposes the FIFO engine so future LIFO implementations can swap in.
    - User Story: As the treasury module, I need GST summaries to capture input/output ledgers.
      - Tasks:
        - Create `backend/app/services/gst_service.py` functions to log `GSTLedger` entries based on purchase/sale payloads.
        - Build `backend/app/factories/gst_factory.py` to surface the GST calculator interface.
        - Develop `backend/app/api/v1/routes/gst.py` to expose `/gst/summary` that aggregates `gst_input`, `gst_output`, and `difference`.
    - User Story: As a profit analyst, I want aggregated metrics so dashboards can chart performance.
      - Tasks:
        - Flesh out `backend/app/services/profit_service.py` to aggregate sales totals, COGS, and expenses, returning gross/net profit.
        - Define `ProfitSummary` in `backend/app/schemas/analytics_schema.py`.
        - Hook `backend/app/api/v1/routes/analytics.py` to serve `/analytics/profit-summary` and `/analytics/stock-levels`.

- **Phase C – Frontend UI & Token Flow**
  - Epic: Authentication & layout
    - User Story: As a user, I want to log in via the Next.js UI so I can access protected views.
      - Tasks:
        - Implement `frontend/services/authService.ts` with `login(username, password)` that calls `/auth/login` via `apiRequest` and stores tokens (cookies or `localStorage`).
        - Build `frontend/hooks/useAuth.ts` to provide `login`, `logout`, and `user` state, reusing `authService`.
        - Update `frontend/app/login/page.tsx` to render a form, call `useAuth().login`, and navigate to `/dashboard` on success.
  - Epic: Dashboard & feature pages
    - User Story: As a staff member, I want a dashboard overview so I can monitor KPIs.
      - Tasks:
        - Complete `frontend/services/analyticsService.ts` with `fetchProfitSummary` and `fetchStockLevels`.
        - Implement `frontend/app/dashboard/page.tsx` to render summary `Card` components, a `Chart`, and fetch analytics data on the server/client.
        - Update `frontend/components/Card.tsx` or `Chart.tsx` as needed to accept dynamic props (title, value, trend).
    - User Story: As an operations user, I want item/purchase/sale pages to talk to the API.
      - Tasks:
        - Fill `frontend/services/itemsService.ts`, `purchaseService.ts`, `salesService.ts` with CRUD wrappers using `apiRequest`.
        - Build minimal UIs in `frontend/app/items/page.tsx`, `purchases/page.tsx`, and `sales/page.tsx` that submit forms to the services and show tables/lists of entries.
        - Hook the shared `Sidebar`/`Navbar` so navigation links render across feature pages.

- **Phase D – Reporting, Documents & Deployment**
  - Epic: Document uploads & exports
    - User Story: As an admin, I want to upload purchase/sale documents so records stay auditable.
      - Tasks:
        - Implement `/documents/upload` router in `backend/app/api/v1/routes/documents.py` accepting multipart uploads and storing metadata in `Document`.
        - Extend `frontend/app/documents/page.tsx` with a file picker that POSTs to the backend.
        - Add `frontend/services/documentService.ts` with `uploadDocument(formData)` and `listDocuments`.
    - User Story: As a manager, I want CSV/Excel/PDF exports so I can share reports.
      - Tasks:
        - Build `backend/app/api/v1/routes/reports.py` with `/reports/sales` that checks `format` query param and streams CSV/XLSX/PDF.
        - Add `frontend/services/reportService.ts` (or extend `analyticsService`) to download reports via `fetch`.
  - Epic: GitOps & containers
    - User Story: As the ops lead, I want runnable Dockerfiles so the stack can run locally/in production.
      - Tasks:
        - Harden `backend/Dockerfile` and `frontend/Dockerfile` for multi-stage builds (install deps, copy source, expose ports).
        - Update root `docker-compose.yml` to orchestrate backend, frontend, and Postgres, wiring env vars and volumes.
        - Document startup steps in `README.md` referencing `docker/scripts/init_db.sh` and `docker/scripts/startup.sh`.

> **Next Step:** I’ve captured the full roadmap in `docs/system_roadmap.md`; pick any single task above and let me know when you’d like me to work on it.
