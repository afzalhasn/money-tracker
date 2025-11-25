#!/bin/bash

# Script to create frontend folder structure (Next.js 14)

# App routes
mkdir -p app/{login,dashboard,items,purchases,sales,expenses,investments,documents,analytics}
touch app/login/page.jsx
touch app/dashboard/page.jsx
touch app/items/page.jsx
touch app/purchases/page.jsx
touch app/sales/page.jsx
touch app/expenses/page.jsx
touch app/investments/page.jsx
touch app/documents/page.jsx
touch app/analytics/page.jsx
touch app/{layout.jsx,globals.css,middleware.js}

# Components
mkdir -p components
touch components/{Navbar.jsx,Sidebar.jsx,Card.jsx,Chart.jsx,Loader.jsx}

# Services
mkdir -p services
touch services/{apiClient.js,authService.js,itemsService.js,purchaseService.js,salesService.js,expenseService.js,investmentService.js,analyticsService.js,gstService.js,documentService.js}

# Hooks
mkdir -p hooks
touch hooks/{useAuth.js,useApi.js}

# Utils
mkdir -p utils
touch utils/helpers.js

# Public
mkdir -p public

# Root frontend files
touch Dockerfile package.json

echo "✅ Frontend structure created successfully!"
