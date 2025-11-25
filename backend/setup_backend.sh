#!/bin/bash

# Script to create backend folder structure (FastAPI)

# API
mkdir -p api/v1/routes
touch api/__init__.py api/v1/__init__.py
touch api/v1/routes/{auth.py,items.py,purchases.py,sales.py,expenses.py,investments.py,analytics.py,gst.py,documents.py,reports.py}

# Core
mkdir -p core
touch core/{config.py,security.py,logging.py,utils.py}

# DB
mkdir -p db/models db/migrations/versions
touch db/{base.py,session.py,__init__.py}
touch db/models/{user.py,item.py,purchase_batch.py,sale.py,expense.py,investment.py,document.py,gst_ledger.py,__init__.py}
touch db/migrations/{env.py,README}

# Factories
mkdir -p factories
touch factories/{inventory_factory.py,gst_factory.py,profit_factory.py,storage_factory.py,__init__.py}

# Services
mkdir -p services
touch services/{fifo_service.py,gst_service.py,profit_service.py,document_service.py,__init__.py}

# Schemas
mkdir -p schemas
touch schemas/{auth_schema.py,user_schema.py,item_schema.py,purchase_schema.py,sale_schema.py,expense_schema.py,investment_schema.py,analytics_schema.py,gst_schema.py,document_schema.py,__init__.py}

# Uploads
mkdir -p uploads/{purchases,sales,misc}

# Tests
mkdir -p tests
touch tests/{test_auth.py,test_fifo.py,test_gst.py,test_profit.py,test_crud_items.py,test_crud_transactions.py,__init__.py}

# Root backend files
touch main.py requirements.txt Dockerfile README.md

echo "✅ Backend structure created successfully!"
