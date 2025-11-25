#!/bin/bash

# Money Tracker App Folder Structure Script

# Root level
mkdir -p root/{backend,frontend,docker,docs,.github/workflows}
touch root/.env root/docker-compose.yml root/README.md

##############################
# Backend (FastAPI)
##############################
mkdir -p root/backend/api/v1/routes
mkdir -p root/backend/core
mkdir -p root/backend/db/{models,migrations/versions}
mkdir -p root/backend/factories
mkdir -p root/backend/services
mkdir -p root/backend/schemas
mkdir -p root/backend/uploads/{purchases,sales,misc}
mkdir -p root/backend/tests

# Backend files
touch root/backend/api/__init__.py
touch root/backend/api/v1/__init__.py
touch root/backend/api/v1/routes/{auth.py,items.py,purchases.py,sales.py,expenses.py,investments.py,analytics.py,gst.py,documents.py,reports.py}

touch root/backend/core/{config.py,security.py,logging.py,utils.py}

touch root/backend/db/{base.py,session.py,__init__.py}
touch root/backend/db/models/{user.py,item.py,purchase_batch.py,sale.py,expense.py,investment.py,document.py,gst_ledger.py,__init__.py}
touch root/backend/db/migrations/{env.py,README}

touch root/backend/factories/{inventory_factory.py,gst_factory.py,profit_factory.py,storage_factory.py,__init__.py}
touch root/backend/services/{fifo_service.py,gst_service.py,profit_service.py,document_service.py,__init__.py}
touch root/backend/schemas/{auth_schema.py,user_schema.py,item_schema.py,purchase_schema.py,sale_schema.py,expense_schema.py,investment_schema.py,analytics_schema.py,gst_schema.py,document_schema.py,__init__.py}

touch root/backend/tests/{test_auth.py,test_fifo.py,test_gst.py,test_profit.py,test_crud_items.py,test_crud_transactions.py,__init__.py}

touch root/backend/{main.py,requirements.txt,Dockerfile,README.md}

##############################
# Frontend (Next.js 14)
##############################
mkdir -p root/frontend/app/{login,dashboard,items,purchases,sales,expenses,investments,documents,analytics}
mkdir -p root/frontend/components
mkdir -p root/frontend/services
mkdir -p root/frontend/hooks
mkdir -p root/frontend/utils
mkdir -p root/frontend/public

# Frontend files
touch root/frontend/app/login/page.jsx
touch root/frontend/app/dashboard/page.jsx
touch root/frontend/app/items/page.jsx
touch root/frontend/app/purchases/page.jsx
touch root/frontend/app/sales/page.jsx
touch root/frontend/app/expenses/page.jsx
touch root/frontend/app/investments/page.jsx
touch root/frontend/app/documents/page.jsx
touch root/frontend/app/analytics/page.jsx
touch root/frontend/app/{layout.jsx,globals.css,middleware.js}

touch root/frontend/components/{Navbar.jsx,Sidebar.jsx,Card.jsx,Chart.jsx,Loader.jsx}
touch root/frontend/services/{apiClient.js,authService.js,itemsService.js,purchaseService.js,salesService.js,expenseService.js,investmentService.js,analyticsService.js,gstService.js,documentService.js}
touch root/frontend/hooks/{useAuth.js,useApi.js}
touch root/frontend/utils/helpers.js

touch root/frontend/{Dockerfile,package.json}

##############################
# Docker
##############################
mkdir -p root/docker/scripts
touch root/docker/{backend.Dockerfile,frontend.Dockerfile,nginx.conf}
touch root/docker/scripts/{init_db.sh,startup.sh}

##############################
# GitHub Actions (CI/CD)
##############################
touch root/.github/workflows/{backend_tests.yml,frontend_tests.yml,deploy.yml}

##############################
# Docs
##############################
touch root/docs/{README.md,architecture.md,api_spec.md,development_plan.md,folder_structure.md}

echo "✅ Money Tracker folder structure created successfully!"
