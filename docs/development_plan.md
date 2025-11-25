# Development Plan (Phase-by-Phase)

This document provides a **step‑by‑step blueprint** for implementing the **Money Tracker Application**, covering backend + frontend setup, database, business logic, dashboard, exports, testing, and deployment.

Each phase is self-contained so you can stop and resume development anytime.

---

# ✅ Phase A — Project Setup

## 🎯 Goals

* Initialize **monorepo** structure
* Set up **Docker + Docker Compose**
* Create basic **FastAPI backend** and **Next.js frontend**
* Configure shared `.env` files
* Prepare for CI/CD and testing

## 📁 Tasks

### 1. Create Monorepo

```
root/
 ├── backend/
 ├── frontend/
 ├── docs/
 ├── docker/
 └── .env
```

### 2. Initialize Backend

* Create FastAPI project
* Add router structure (`api/v1`)
* Add CORS
* Add health check: `/health`
* Add Dockerfile

### 3. Initialize Frontend

* Create Next.js app using App Router
* Install TailwindCSS
* Add initial pages: `/login`, `/dashboard`
* Add Dockerfile

### 4. Docker Compose Setup

Services:

* backend
* frontend
* postgres
* pgadmin (optional)

### 5. Create CI/CD Directories

```
root/.github/workflows/api.yml
```

### 6. Output for Phase A

* Backend builds successfully
* Frontend loads on browser
* Containers orchestrated with Docker Compose

---

# ✅ Phase B — Database & CRUD

## 🎯 Goals

* Create full PostgreSQL schema
* Add SQLAlchemy ORM models
* Implement Alembic migrations
* Implement CRUD for all entities

## 📁 Tasks

### 1. Define Models

* Users
* Items
* PurchaseBatches
* Sales
* Expenses
* Investments
* Documents
* GST Ledger

### 2. Create Alembic Migration

* Automap all models
* Generate initial migration

### 3. CRUD Endpoints

* /items
* /purchases
* /sales
* /expenses
* /investments
* /documents (meta only)

### 4. Output for Phase B

* All CRUD APIs functional
* Database seeded with test data

---

# ✅ Phase C — Business Logic

## 🎯 Goals

* Implement FIFO algorithm
* Implement COGS calculation
* Implement GST input/output logic
* Implement profit engine (gross, net profit)

## 📁 Tasks

### 1. FIFO Engine

* Deduct batches in chronological order
* Manage partial batch consumption

### 2. COGS Engine

* Multiply consumed stock × purchase rate

### 3. GST Engine

* Calculate GST input on purchases
* Calculate GST output on sales

### 4. Profit Engine

Gross Profit = Sales − COGS
Net Profit = Gross − Expenses

### 5. Abstract Factory Integration

Create factories for:

* Inventory (FIFO)
* GST
* Profit
* Storage (Local)

### 6. Output for Phase C

* All business logic functional via API
* All engines integrated via Abstract Factory

---

# ✅ Phase D — Dashboard, Exports, Uploads

## 🎯 Goals

* Build dashboard UI with Charts.js
* Create export engine (CSV, Excel, PDF)
* Integrate document uploads

## 📁 Tasks

### 1. Dashboard

* Build cards (sales, purchases, profit)
* Profit chart (line chart)
* Category-wise bar chart
* Low stock alerts

### 2. Reports Export

* CSV using Python CSV writer
* Excel using openpyxl
* PDF using ReportLab

### 3. Document Upload

* Implement `/documents/upload`
* Store files in `/uploads`
* Link documents with transactions

### 4. Output for Phase D

* Fully functional dashboard
* Export system working for all formats
* Uploads working locally

---

# ✅ Phase E — Authentication, Roles, Testing

## 🎯 Goals

* Implement JWT access + refresh tokens
* Create Admin/Staff roles
* Write unit tests for business logic
* Add API validations

## 📁 Tasks

### 1. Auth

* `/auth/register`
* `/auth/login`
* `/auth/refresh`

### 2. Roles

* Admin can manage categories
* Staff cannot access analytics or GST

### 3. Testing

* Unit test FIFO engine
* Unit test GST engine
* Unit test profit engine
* Test CRUD APIs

### 4. Output for Phase E

* Application secure with RBAC
* All major logic covered by tests

---

# ✅ Phase F — Deployment & Production

## 🎯 Goals

* Harden the application
* Prepare for production deployment
* Build optimized images

## 📁 Tasks

### 1. Docker Production Build

* Multi-stage Dockerfile for backend
* Multi-stage Dockerfile for frontend

### 2. NGINX Reverse Proxy

* Configure SSL (optional)
* Route frontend + backend

### 3. Environment Configuration

* `.env.production`
* Secure JWT secrets

### 4. Optional CI/CD

* GitHub Actions pipeline
* Auto deploy to VPS / AWS EC2

### 5. Output for Phase F

* Application ready for production

---

# ✔ Completed

Next file to generate:
**docs/folder_structure.md**
