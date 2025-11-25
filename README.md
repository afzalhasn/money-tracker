# Money Tracker Application

## Overview

The **Money Tracker** application is a full‑stack solution designed for small businesses to track and manage their daily financial operations, including purchases, sales, expenses, inventory, GST, documents, and profit analytics.

The application prioritizes:

* Clean, simple user experience
* Accurate accounting calculations
* FIFO‑based inventory and COGS computation
* Modern UI using Next.js
* Scalable backend architecture using FastAPI and Abstract Factory Pattern
* Robust PostgreSQL database schema
* Full documentation and step‑by‑step development phases

---

## Core Objectives

* Provide business owners an efficient way to track daily operations.
* Offer staff an easy interface for data entry.
* Maintain reliable, accurate profit computation using FIFO.
* Support GST input/output calculations.
* Deliver a beautiful dashboard with actionable insights.
* Allow document uploads (receipts, invoices, etc.).
* Provide exportable reports (CSV, Excel, PDF).

---

## Feature Set (Version 1)

### **1. Transactions**

* Purchases
* Sales
* Expenses
* Investments

### **2. Inventory Management**

* FIFO batches
* Auto stock reduction on sales
* COGS calculation
* Low stock alerts

### **3. Accounting & Profit Engine**

* Gross Profit
* Net Profit
* GST Input vs Output

### **4. Dashboard**

* Sales, purchases, expenses, investments
* Profit trends
* Inventory status
* Category‑wise analytics

### **5. User Management**

* Admin & Staff roles
* Authentication using JWT

### **6. Document Uploads**

* Purchase bills
* Sales receipts

### **7. Reports**

* Export CSV
* Export Excel
* Export PDF

---

## Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** Next.js 14 (App Router) + TailwindCSS
* **Database:** PostgreSQL
* **Storage:** Local (V1), S3 upcoming
* **Auth:** JWT
* **Docs:** Swagger/OpenAPI
* **Deployment:** Docker & Docker Compose
* **Design Pattern:** Abstract Factory (Backend)

---

## Phase Breakdown

* **Phase A:** Setup (Monorepo, Docker, Basic Services)
* **Phase B:** Database & CRUD
* **Phase C:** Business Logic (FIFO, GST, Profit)
* **Phase D:** Dashboard & Reporting
* **Phase E:** Testing & User Roles
* **Phase F:** Deployment & Production Readiness

---

## Folder Structure (Simplified Preview)

A full detailed structure is provided in `folder_structure.md`.

```
root/
 ├── backend/
 ├── frontend/
 ├── docs/
 └── docker/
```

---

## Next Steps

Proceed to: **docs/architecture.md**
