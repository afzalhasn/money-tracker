# System Architecture Summary

## Backend
- FastAPI (see `backend/app/main.py`) exposes a single FastAPI instance with CORS and a health endpoint; `backend/app/core/config.py` centralizes settings such as JWT secrets, database URL, and prefixes while `backend/app/db/session.py` wires SQLAlchemy to `SessionLocal` backed by that config.
- Business entities live under `backend/app/db/models/` (Users, Items, PurchaseBatch, Sale, Expense, Investment, Document, GSTLedger) with relationships wired to `Base` from `backend/app/db/base.py`. Schemas under `backend/app/schemas/` describe the expected request/response shapes, and `backend/app/api/v1/routes/` is where each domain (items, purchases, sales, expenses, investments, analytics, GST, documents, auth, reports) will expose FastAPI routers.
- The remaining backend pillars are service layers (`backend/app/services/`) that will implement FIFO/GST/profit/document logic, and the factory packages (`backend/app/factories/`) that will eventually provide concrete engines for inventory, GST, profit, and storage adapters.

## Frontend
- A Next.js App Router application lives under `frontend/app/` with entry pages for login, dashboard, items, purchases, sales, expenses, investments, documents, and analytics. `frontend/app/layout.tsx` and `globals.css` share layout and styling decisions, while `middleware.ts` is the hook point for auth enforcement.
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
        - [x] Define `ItemUpdate` in `backend/app/schemas/item_schema.py` so updates stay typed while reusing existing DTOs.
        - [x] Implement `backend/app/services/item_service.py` with `create_item`, `get_item`, and `list_items` functions that open a session, call the `Item` model, and return ORM objects.
        - [x] Build `backend/app/api/v1/routes/items.py` to mount a `router = APIRouter(prefix="/items")` exposing `POST /items/` and `GET /items/` using the new service and schemas.
    - User Story: As a backend developer, I need purchases to create FIFO batches so stock tracking begins.
    - Tasks:
        - [x] Expand `backend/app/schemas/purchase_schema.py` with `PurchaseCreate` and `PurchaseRead` models covering `item_id`, `quantity`, `rate`, `gst_percent`, `invoice_number`, and timestamps.
        - [x] Add `backend/app/services/purchase_service.py` with `create_purchase_batch` that persists `PurchaseBatch` and `list_purchase_batches` that returns recent entries.
        - [x] Wire `backend/app/api/v1/routes/purchases.py` to accept POST payloads, call the service, and emit the `PurchaseRead` response.
    - User Story: As a backend developer, I need sales creation to exercise FIFO deductions via a simple endpoint.
      - Tasks:
        - [x] Add `SaleCreate`/`SaleRead` models inside `backend/app/schemas/sale_schema.py` describing sell quantity, rate, GST, COGS, and remaining stock.
        - [x] Implement `backend/app/services/sale_service.py` with FIFO allocation logic that adjusts purchase batches, computes COGS, and persists `Sale` records.
        - [x] Implement `backend/app/api/v1/routes/sales.py` with POST/GET handlers wired to the new service and returning paginated sale data.
    - User Story: As a backend developer, I want the Phase A APIs covered by automated regression tests before Phase B work begins.
      - Tasks:
        - [x] Add pytest suites under `backend/tests/` that exercise `/items/`, `/purchases/`, and `/sales/` through FastAPI's `TestClient`.
        - [x] Provide a data-generation helper script so the tests can bootstrap items, purchase batches, and sales deterministically.

- **Phase B – Business Logic & Analytics**
  - Epic: FIFO + GST engines
    - User Story: As the accounting engine, I want FIFO deduction logic to compute COGS for every sale.
      - Tasks:
        - [x] Implement `backend/app/services/fifo_service.py` logic to fetch oldest `PurchaseBatch` rows, subtract quantities, and return consumed batches.
        - [x] Persist COGS results inside `Sale` records during `create_sale`.
        - [x] Create `backend/app/factories/inventory_factory.py` that exposes the FIFO engine so future LIFO implementations can swap in.
    - User Story: As the treasury module, I need GST summaries to capture input/output ledgers.
      - Tasks:
        - [x] Create `backend/app/services/gst_service.py` functions to log `GSTLedger` entries based on purchase/sale payloads.
        - [x] Build `backend/app/factories/gst_factory.py` to surface the GST calculator interface.
        - [x] Develop `backend/app/api/v1/routes/gst.py` to expose `/gst/summary` that aggregates `gst_input`, `gst_output`, and `difference`.
    - User Story: As a profit analyst, I want aggregated metrics so dashboards can chart performance.
      - Tasks:
        - [x] Flesh out `backend/app/services/profit_service.py` to aggregate sales totals, COGS, and expenses, returning gross/net profit.
        - [x] Define `ProfitSummary` in `backend/app/schemas/analytics_schema.py`.
        - [x] Hook `backend/app/api/v1/routes/analytics.py` to serve `/analytics/profit-summary` and `/analytics/stock-levels`.

---

- **Phase C – UI/UX Foundation & Design System**
  - Epic: Global Styling & Design Tokens
    - User Story: As a designer, I need a cohesive theme so every page looks modern and consistent.
      - Tasks:
        - [x] Configure Tailwind CSS in the Next.js app and align it with TypeScript tooling.
        - [x] Define design tokens via the Tailwind config and `globals.css`, covering colors (background, surface, primary, danger, border, text), typography, spacing, radius, and shadows.
        - [x] Establish base styles in `globals.css`, including resets, body background, and typography defaults.
        - [x] Ship core shadcn/ui atoms (Button, Input, Card, Dialog, Dropdown, Skeleton) so every component shares the same foundation.
        - [x] Create layout utilities (Page container, section header patterns) built from Tailwind + shadcn primitives.

- **Phase D – App Shell, Navigation & Layout**
  - Epic: Shared Layout Framework
    - User Story: As a user, I want a reliable shell (Navbar + Sidebar + Content) so navigation feels stable across screens.
      - Tasks:
        - [x] Style the Navbar and Sidebar with Tailwind + shadcn Cards/Buttons and Lucide iconography plus hover/active states.
        - [x] Add responsive behavior so the sidebar collapses gracefully on small screens.
        - [x] Build shared layout components (`PageContainer`, `PageHeader`, `PageSection`) that encapsulate spacing and backgrounds.
        - [x] Update `app/layout.tsx` so every page renders inside the global shell built from these helpers.

- **Phase E – Dashboard (UI-First, API-Second)**
  - Epic: Stunning Dashboard UI
    - User Story: As a stakeholder, I want a best-looking dashboard prototype so designers and engineers share a visual benchmark.
      - Tasks:
        - [x] Implement a reusable `StatCard` (shadcn Card + Lucide icon) with props for `title`, `value`, `description?`, `trend?`, and `icon?`.
        - [x] Integrate `react-chartjs-2` + Chart.js and expose styled Line/Bar chart components that match the theme.
        - [x] Build `app/dashboard/page.tsx` using mock data only, showing KPI cards (profit, revenue, expenses, stock value) and 1–2 charts (profit/sales trends).
        - [x] Add loading skeletons (shadcn Skeleton) for the cards and charts before hooking into APIs.
        - [x] Avoid backend calls in this phase; focus purely on visual polish and UX interactions.

- **Phase F – Feature Pages (UI-First, Reusable Patterns)**
  - Epic: Consistent CRUD Pages
    - User Story: As an operations user, I want every CRUD/reporting page to honor the same layout & controls.
      - Tasks:
        - Use `PageHeader` for titles/actions and `PageContainer` for padding/backdrop on each page.
        - Build all forms with React Hook Form + Zod, leveraging shadcn `Input`, `Select`, `Button`, and `Dialog` for modals.
        - Provide shared table/list components (or shadcn table equivalents) plus optional filter/search bars.
        - Prototype UI (mock data only) for Items, Purchases, Sales, Expenses, Investments, GST Summary, and Documents pages before wiring APIs.
        - Verify each mock page adheres to the design-system spacing, colors, typography, and components.

- **Phase G – API Integration for Frontend (Connect All Backend Endpoints)**
  - Epic: Wire Frontend to Backend via Typed Services
    - User Story: As a developer, I want a typed service layer so every frontend route reuses the same TanStack Query wrappers.
      - Tasks:
        - Create a shared API client (`fetch` or `axios`) wrapped with TanStack Query, using `NEXT_PUBLIC_API_BASE_URL` and attaching auth tokens.
        - Build service modules matching backend routes (`itemsService`, `purchaseService`, `salesService`, `expensesService`, `investmentsService`, `gstService`, `analyticsService`, `documentService`).
        - Replace mock data on each Phase F page with `useQuery`/`useMutation` hooks (loading/error states handled with shadcn Skeleton + Toasts).
        - Confirm every CRUD/analytics flow works end-to-end and every defined backend API is used by a UI surface.

- **Phase H – Authentication & Route Protection**
  - Epic: Login & Token Flow
    - User Story: As a secure platform user, I want to log in/out seamlessly so protected pages stay locked down.
      - Tasks:
        - Implement `authService` calling `/auth/login` (and `/auth/refresh` if available) and persisting tokens.
        - Build a `useAuth` hook wrapping TanStack Query/local state that exposes `login`, `logout`, and `isAuthenticated`.
        - Style `/login` with shadcn form components, React Hook Form, and Zod validation.
        - Apply route guards: use Next.js middleware to redirect unauthenticated users and optionally wrap authenticated areas in a `ProtectedLayout`.

- **Phase I – UX Polish & Quality**
  - Epic: Premium Feel
    - User Story: As a product manager, I want delightful motion, toasts, and dark mode so the experience feels premium.
      - Tasks:
        - Show toast notifications for all important actions and surface field-level + summary validation messages.
        - Add micro-animations (hover states, transitions, page transitions) using Tailwind/optional Framer Motion.
        - Implement dark mode via CSS variables/Tailwind themes plus style 404/500 pages to match the app.

- **Phase J – Frontend UI & Token Flow**
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

- **Phase K – Reporting, Documents & Deployment**
  - Epic: Document uploads & exports
    - User Story: As an admin, I want to upload purchase/sale documents so records stay auditable.
      - Tasks:
        - Implement `/documents/upload` router in `backend/app/api/v1/routes/documents.py` accepting multipart uploads and storing metadata in `Document`.
        - Extend `frontend/app/documents/page.tsx` with a file picker that POSTs to the backend.
        - Add `frontend/services/documentService.ts` with `uploadDocument(formData)` and `listDocuments`.
  - Epic: GitOps & containers
    - User Story: As the ops lead, I want runnable Dockerfiles so the stack can run locally/in production.
      - Tasks:
        - Harden `backend/Dockerfile` and `frontend/Dockerfile` for multi-stage builds (install deps, copy source, expose ports).
        - Update root `docker-compose.yml` to orchestrate backend, frontend, and Postgres, wiring env vars and volumes.
        - Document startup steps in `README.md` referencing `docker/scripts/init_db.sh` and `docker/scripts/startup.sh`.
