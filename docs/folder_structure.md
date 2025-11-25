# Folder Structure (Backend + Frontend + Docker + CI/CD)

This document defines the **complete, production-ready folder structure** for the Money Tracker Application.
The structure supports modularity, testing, abstract factory pattern, CI/CD, and scalability.

---

# 1. Root Directory Structure

```
root/
 ├── backend/
 ├── frontend/
 ├── docker/
 ├── docs/
 ├── .env
 ├── docker-compose.yml
 └── README.md
```

---

# 2. Backend Folder Structure (FastAPI)

```
backend/
 ├── api/
 │   ├── v1/
 │   │   ├── routes/
 │   │   │   ├── auth.py
 │   │   │   ├── items.py
 │   │   │   ├── purchases.py
 │   │   │   ├── sales.py
 │   │   │   ├── expenses.py
 │   │   │   ├── investments.py
 │   │   │   ├── analytics.py
 │   │   │   ├── gst.py
 │   │   │   ├── documents.py
 │   │   │   └── reports.py
 │   │   └── __init__.py
 │   └── __init__.py
 │
 ├── core/
 │   ├── config.py
 │   ├── security.py
 │   ├── logging.py
 │   └── utils.py
 │
 ├── db/
 │   ├── base.py
 │   ├── session.py
 │   ├── models/
 │   │   ├── user.py
 │   │   ├── item.py
 │   │   ├── purchase_batch.py
 │   │   ├── sale.py
 │   │   ├── expense.py
 │   │   ├── investment.py
 │   │   ├── document.py
 │   │   ├── gst_ledger.py
 │   │   └── __init__.py
 │   ├── migrations/
 │   │   ├── env.py
 │   │   ├── versions/
 │   │   └── README
 │   └── __init__.py
 │
 ├── factories/
 │   ├── inventory_factory.py
 │   ├── gst_factory.py
 │   ├── profit_factory.py
 │   ├── storage_factory.py
 │   └── __init__.py
 │
 ├── services/
 │   ├── fifo_service.py
 │   ├── gst_service.py
 │   ├── profit_service.py
 │   ├── document_service.py
 │   └── __init__.py
 │
 ├── schemas/
 │   ├── auth_schema.py
 │   ├── user_schema.py
 │   ├── item_schema.py
 │   ├── purchase_schema.py
 │   ├── sale_schema.py
 │   ├── expense_schema.py
 │   ├── investment_schema.py
 │   ├── analytics_schema.py
 │   ├── gst_schema.py
 │   ├── document_schema.py
 │   └── __init__.py
 │
 ├── uploads/
 │   ├── purchases/
 │   ├── sales/
 │   └── misc/
 │
 ├── tests/
 │   ├── test_auth.py
 │   ├── test_fifo.py
 │   ├── test_gst.py
 │   ├── test_profit.py
 │   ├── test_crud_items.py
 │   ├── test_crud_transactions.py
 │   └── __init__.py
 │
 ├── main.py
 ├── requirements.txt
 ├── Dockerfile
 └── README.md
```

---

# 3. Frontend Structure (Next.js 14)

```
frontend/
 ├── app/
 │   ├── login/
 │   │   └── page.jsx
 │   ├── dashboard/
 │   │   └── page.jsx
 │   ├── items/
 │   │   └── page.jsx
 │   ├── purchases/
 │   │   └── page.jsx
 │   ├── sales/
 │   │   └── page.jsx
 │   ├── expenses/
 │   │   └── page.jsx
 │   ├── investments/
 │   │   └── page.jsx
 │   ├── documents/
 │   │   └── page.jsx
 │   ├── analytics/
 │   │   └── page.jsx
 │   ├── layout.jsx
 │   ├── globals.css
 │   └── middleware.js
 │
 ├── components/
 │   ├── Navbar.jsx
 │   ├── Sidebar.jsx
 │   ├── Card.jsx
 │   ├── Chart.jsx
 │   └── Loader.jsx
 │
 ├── services/
 │   ├── apiClient.js
 │   ├── authService.js
 │   ├── itemsService.js
 │   ├── purchaseService.js
 │   ├── salesService.js
 │   ├── expenseService.js
 │   ├── investmentService.js
 │   ├── analyticsService.js
 │   ├── gstService.js
 │   └── documentService.js
 │
 ├── hooks/
 │   ├── useAuth.js
 │   └── useApi.js
 │
 ├── utils/
 │   └── helpers.js
 │
 ├── public/
 ├── Dockerfile
 └── package.json
```

---

# 4. Docker Directory

```
docker/
 ├── backend.Dockerfile
 ├── frontend.Dockerfile
 ├── nginx.conf
 └── scripts/
     ├── init_db.sh
     └── startup.sh
```

---

# 5. CI/CD Structure (GitHub Actions)

```
.github/
 └── workflows/
     ├── backend_tests.yml
     ├── frontend_tests.yml
     └── deploy.yml
```

---

# 6. Docs Directory

```
docs/
 ├── README.md
 ├── architecture.md
 ├── api_spec.md
 ├── development_plan.md
 └── folder_structure.md
```

---

# 7. Summary

This folder structure ensures:

* Clean separation of backend, frontend, and infrastructure
* Abstract factory ready backend services
* Modular frontend with services/hooks
* Scalable Docker deployment
* Organized tests and CI/CD pipelines

The entire application is now fully documented.

Next step: Begin **Phase A — Implementation Setup** (monorepo + Docker).
