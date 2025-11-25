# API Specification (OpenAPI Style)

## Overview

This document provides the complete API specification for the **Money Tracker Application** backend built using **FastAPI**. All endpoints follow REST standards and return JSON responses unless specified.

Authentication uses **JWT (Access + Refresh Tokens)**.

---

# 1. Authentication API

## **POST /auth/register**

Register a new user (Admin creates staff).

**Request Body:**

```json
{
  "username": "john",
  "password": "123456",
  "full_name": "John Doe",
  "role": "ADMIN"
}
```

**Response:**

```json
{
  "id": "uuid",
  "username": "john",
  "role": "ADMIN"
}
```

---

## **POST /auth/login**

Login and receive tokens.

```json
{
  "username": "john",
  "password": "123456"
}
```

**Response:**

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}
```

---

## **POST /auth/refresh**

Refresh the access token.

```json
{
  "refresh_token": "..."
}
```

**Response:**

```json
{
  "access_token": "..."
}
```

---

# 2. Items API

## **POST /items/**

Create a new item.

```json
{
  "name": "Rice",
  "unit": "kg",
  "low_stock_threshold": 20
}
```

---

## **GET /items/**

List all items.

---

## **GET /items/{item_id}**

Retrieve a single item.

---

## **PUT /items/{item_id}**

Update item details.

---

## **DELETE /items/{item_id}**

Delete an item.

---

# 3. Purchases API

## **POST /purchases/**

Create a purchase entry **and generate FIFO batch**.

```json
{
  "item_id": "uuid",
  "quantity": 50,
  "rate": 100,
  "gst_percent": 5,
  "invoice_number": "INV001"
}
```

---

## **GET /purchases/**

List all purchase records.

---

# 4. Sales API

## **POST /sales/**

Create sale entry and auto-deduct stock using FIFO.

```json
{
  "item_id": "uuid",
  "quantity": 80,
  "rate": 150,
  "gst_percent": 5
}
```

**Response:**

```json
{
  "sale_id": "uuid",
  "cogs": 8300,
  "remaining_stock": 20
}
```

---

## **GET /sales/**

List all sales.

---

# 5. Expenses API

## **POST /expenses/**

```json
{
  "category": "Transport",
  "amount": 1200,
  "note": "Delivery to client"
}
```

---

## **GET /expenses/**

List expenses.

---

# 6. Investments API

## **POST /investments/**

```json
{
  "investor_name": "Investor 1",
  "amount": 50000
}
```

---

## **GET /investments/**

List investments.

---

# 7. FIFO & Profit Engine APIs

## **GET /analytics/profit-summary**

Return profit statistics.

**Response:**

```json
{
  "total_sales": 12600,
  "cogs": 8300,
  "gross_profit": 4300,
  "net_profit": 2600
}
```

---

## **GET /analytics/stock-levels**

Return stock with low-stock alerts.

---

# 8. GST API

## **GET /gst/summary**

Breakdown of input/output GST.

**Response:**

```json
{
  "gst_input": 525,
  "gst_output": 600,
  "difference": 75
}
```

---

# 9. Document Upload API

## **POST /documents/upload**

Upload invoice/receipt.

**Multipart Form-Data:**

* file
* transaction_id
* type (purchase/sale)

---

## **GET /documents/{doc_id}**

Serve file download.

---

# 10. Reports API

## **GET /reports/sales?format=csv**

Exports sales as CSV/Excel/PDF.

Formats:

* csv
* xlsx
* pdf

---

# 11. Admin API

## **POST /admin/categories**

Add expense categories.

---

# 12. Error Response Format

All endpoints return consistent error output:

```json
{
  "detail": "Error message here"
}
```

---

# 13. Security Notes

* All `/admin/*` routes require role = ADMIN.
* Staff cannot edit categories or view GST/profit dashboards.
* JWT required for all routes except `/auth/*`.

---

# Next Steps

Proceed to: **docs/development_plan.md**
