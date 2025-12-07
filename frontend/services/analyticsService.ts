import { apiRequest } from "./apiClient";

export type ProfitSummary = {
  total_sales: number;
  cogs: number;
  gross_profit: number;
  net_profit: number;
};

export type StockLevel = {
  item_id: string;
  item_name: string;
  stock: number;
  low_stock_threshold: number;
  is_low_stock: boolean;
};

export function fetchProfitSummary(): Promise<ProfitSummary> {
  return apiRequest("/analytics/profit-summary");
}

export function fetchStockLevels(): Promise<StockLevel[]> {
  return apiRequest("/analytics/stock-levels");
}
