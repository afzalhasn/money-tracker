# System Architecture Documentation

## 1. Overview

The **Money Tracker Application** follows a clean, scalable, and modular architecture using:

* **FastAPI** for backend services
* **Next.js 14** for frontend UI
* **PostgreSQL** for relational storage
* **Abstract Factory Pattern** for backend modular business logic
* **Docker Compose** for containerized deployment

This architecture ensures:

* High performance
* Clear separation of concerns
* Easy maintainability
* Extensibility for future phases (mobile app, S3 storage, multi-tenancy, etc.)

---

## 2. High-Level Architecture Diagram

*(Conceptual Overview)*

```
                 ┌───────────────────────┐
                 │      Next.js UI       │
                 │  (Tailwind + Charts)  │
                 └───────────┬───────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   FastAPI API   │
                    │ (Business Layer)│
                    └───────┬─────────┘
                            │
             ┌──────────────┼──────────────────┐
             ▼              ▼                  ▼
      ┌──────────┐   ┌────────────┐    ┌──────────────┐
      │ Postgres │   │ File Upload│    │ Abstract      │
      │ Database │   │ (Local/S3) │    │ Factory Layer │
      └──────────┘   └────────────┘    └──────────────┘
```

---

## 3. Backend Architecture (FastAPI)

### 3.1 Layers

```
backend/
 ├── api/             → API route handlers
 ├── core/            → Config, security, utils
 ├── db/              → Database session, migrations, models
 ├── factories/       → Abstract Factory implementation
 ├── services/        → Business logic (FIFO, GST, Profit)
 ├── schemas/         → Pydantic models
 └── uploads/         → Document storage
```

### 3.2 Design Pattern: Abstract Factory

The backend uses the **Abstract Factory Pattern** to provide interchangeable, modular implementations of:

* Inventory engines (FIFO, future LIFO)
* GST calculation
* Profit engine
* Document storage adapters (local, S3)

#### Benefits:

* Plug-and-play business logic engines
* Easy testing and mocking
* Clean separation of modules
* Future extensibility

### 3.3 Example: Factory Structure

```
/factories
 ├── inventory_factory.py
 ├── gst_factory.py
 ├── profit_factory.py
 └── storage_factory.py
```

Each factory returns a concrete implementation.

---

## 4. Frontend Architecture (Next.js 14)

### 4.1 Key Technologies

* App Router Architecture
* TailwindCSS
* Client & Server Components
* React Query (data fetching + caching)
* Charts.js for dashboard
* Middleware for auth

### 4.2 Recommended Design Pattern: **Module-Based Architecture**

Instead of abstract factory (not ideal for frontend), Next.js should use:

* **Module-based folder structure**
* **Hooks for logic abstraction**
* **Services for API abstraction**
* **Context for auth management**

### Example Structure:

```
frontend/
 ├── app/
 │   ├── dashboard/
 │   ├── purchases/
 │   ├── sales/
 │   ├── expenses/
 │   └── api/ (optional server actions)
 ├── components/
 ├── hooks/
 ├── services/
 └── styles/
```

---

## 5. Database Architecture (PostgreSQL)

### 5.1 Main Entities

* Users
* Items
* Purchase Batches (FIFO)
* Sales
* Expenses
* Investments
* GST Ledger
* Documents

### 5.2 ER Diagram (Simplified)

```
Users (1) ──────── (∞) Purchases
        └───────── (∞) Sales
        └───────── (∞) Expenses

Items (1) ──────── (∞) PurchaseBatches
Items (1) ──────── (∞) Sales
```

Detailed schema provided later in API spec.

---

## 6. Communication Workflow

### Frontend → Backend

* JWT Authentication
* REST API Calls
* File uploads via multipart/form-data

### Backend → Database

* SQLAlchemy ORM
* ACID transactions
* FIFO stock deduction via atomic operations

---

## 7. Security

* JWT Access + Refresh tokens
* bcrypt for password hashing
* Role-based access (Admin/Staff)
* CORS enabled for frontend
* Helmet-like headers in Next.js for hardening

---

## 8. Deployment Architecture

### Local

* docker-compose up

### Production (future)

* Nginx reverse proxy
* S3 file storage
* CI/CD pipelines
* Postgres on managed DB

---

## 9. Summary

The architecture ensures:

* Clean modular backend
* Modern scalable frontend
* Accurate financial computations
* Cloud-ready extensibility

Next file: **docs/api_spec.md**
