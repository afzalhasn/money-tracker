#!/bin/bash

# Create root project folder
mkdir -p money-tracker
cd money-tracker || exit

# Top-level files
touch docker-compose.yml README.md .env

# Backend structure
mkdir -p backend/app/api/v1 \
         backend/app/core \
         backend/app/db/alembic \
         backend/app/schemas \
         backend/app/utils

# Backend files
touch backend/app/main.py \
      backend/app/api/v1/auth.py \
      backend/app/api/v1/purchases.py \
      backend/app/api/v1/sales.py \
      backend/app/api/v1/expenses.py \
      backend/app/api/v1/inventory.py \
      backend/app/api/v1/reports.py \
      backend/app/core/fifo.py \
      backend/app/core/calculations.py \
      backend/app/core/gst.py \
      backend/app/core/exports.py \
      backend/app/db/base.py \
      backend/app/db/models.py \
      backend/app/db/crud.py \
      backend/app/utils/auth_utils.py \
      backend/app/utils/file_utils.py \
      backend/Dockerfile \
      backend/requirements.txt

# Frontend structure
mkdir -p frontend/app/dashboard \
         frontend/app/pages \
         frontend/app/components/charts \
         frontend/app/components/forms \
         frontend/app/components/layout \
         frontend/public/uploads

# Frontend files
touch frontend/next.config.js \
      frontend/package.json \
      frontend/tailwind.config.js

# Database structure
mkdir -p database
touch database/init.sql database/seeds.sql

# Scripts structure
mkdir -p scripts
touch scripts/start-dev.sh scripts/migrate.sh

echo "✅ Project structure created successfully!"

