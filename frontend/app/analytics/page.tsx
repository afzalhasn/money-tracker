"use client";

import { useEffect, useMemo, useState } from "react";
import Card from "@/components/Card";
import Chart from "@/components/Chart";
import { fetchProfitSummary, fetchStockLevels, ProfitSummary, StockLevel } from "@/services/analyticsService";

const placeholderStats = ["Optimizing FIFO", "GST ready", "Real-time KPIs"];

export default function AnalyticsPage() {
  const [profit, setProfit] = useState<ProfitSummary | null>(null);
  const [stocks, setStocks] = useState<StockLevel[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    Promise.all([fetchProfitSummary(), fetchStockLevels()])
      .then(([profitData, stockData]) => {
        if (isMounted) {
          setProfit(profitData);
          setStocks(stockData);
          setError("");
        }
      })
      .catch((err) => {
        console.error(err);
        if (isMounted) {
          setError("Unable to load analytics currently. Try again soon.");
        }
      })
      .finally(() => {
        if (isMounted) {
          setLoading(false);
        }
      });
    return () => {
      isMounted = false;
    };
  }, []);

  const trendData = useMemo(() => [
    profit ? profit.net_profit : 0,
    profit ? profit.gross_profit : 0,
    profit ? profit.cogs : 0,
  ], [profit]);

  const profitCards = useMemo(() => {
    if (!profit) {
      return [];
    }

    return [
      { title: "Total Sales", value: `$${profit.total_sales.toFixed(2)}`, caption: "Gross inflows" },
      { title: "COGS", value: `$${profit.cogs.toFixed(2)}`, caption: "FIFO basis" },
      { title: "Net Profit", value: `$${profit.net_profit.toFixed(2)}`, caption: "After expenses" },
    ];
  }, [profit]);

  const lowStock = stocks.filter((entry) => entry.is_low_stock);

  return (
    <main className="flex min-h-screen w-full flex-col gap-10 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-900 px-8 py-10 text-white">
      <section className="grid gap-8 rounded-[32px] border border-white/10 bg-white/5 p-10 shadow-2xl shadow-black/40 backdrop-blur-xl md:grid-cols-[1.2fr_1fr]">
        <div className="space-y-5">
          <p className="text-xs uppercase tracking-[0.4em] text-slate-400">Analytics</p>
          <h1 className="text-4xl font-semibold leading-tight md:text-5xl">
            Live profit metrics that stay synced with your FIFO engine.
          </h1>
          <p className="max-w-2xl text-base text-slate-200">
            Profit summary, stock levels, and ledger checks all come together through FastAPI. The frontend pulls them
            in and reuses design assets so every metric feels like a cohesive widget.
          </p>
          <div className="flex gap-3 text-xs font-semibold uppercase tracking-[0.4em] text-slate-300">
            {placeholderStats.map((label) => (
              <span key={label} className="rounded-full border border-white/20 px-4 py-2">
                {label}
              </span>
            ))}
          </div>
        </div>
        <div className="space-y-4 rounded-[28px] border border-white/10 bg-slate-900/60 p-6 backdrop-blur-xl">
          <div className="flex items-center justify-between text-[0.6rem] uppercase tracking-[0.4em] text-slate-400">
            <span>Live trend</span>
            <span>{new Date().toLocaleTimeString()}</span>
          </div>
          <div className="text-3xl font-bold text-white">{profit ? `$${profit.net_profit.toFixed(2)}` : "—"}</div>
          <p className="text-sm text-slate-300">Profit after FIFO deductions and expense offsets</p>
          <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
            <Chart data={trendData} className="rounded-xl" />
          </div>
          <div className="text-xs uppercase tracking-[0.4em] text-slate-400">Net vs Gross</div>
        </div>
      </section>

      <section className="space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <h2 className="text-2xl font-semibold">Profit Summary</h2>
          <span className="text-xs uppercase tracking-[0.4em] text-slate-400">Realtime sync</span>
        </div>
        {loading && <div className="text-sm text-slate-400">Loading metrics…</div>}
        {error && <div className="rounded-xl bg-red-500/20 p-4 text-sm text-red-100">{error}</div>}
        <div className="grid gap-5 md:grid-cols-3">
          {profitCards.length > 0
            ? profitCards.map((card) => <Card key={card.title} {...card} />)
            : !loading && <p className="text-sm text-slate-400">No data available yet.</p>}
        </div>
      </section>

      <section className="space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <h2 className="text-2xl font-semibold">Stock Levels</h2>
          <span className="text-xs uppercase tracking-[0.4em] text-slate-400">FIFO batches</span>
        </div>
        <div className="grid gap-4 lg:grid-cols-3">
          {lowStock.map((entry) => (
            <div key={entry.item_id} className="rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-slate-200">
              <div className="flex items-center justify-between text-xs uppercase tracking-[0.4em] text-slate-400">
                <span>{entry.item_name}</span>
                <span>{entry.stock} units</span>
              </div>
              <p className="mt-2 text-xs text-slate-300">Low stock threshold: {entry.low_stock_threshold}</p>
              <p className="mt-1 text-xs text-emerald-300">Remaining lots: {entry.stock}</p>
            </div>
          ))}
          {!lowStock.length && !loading && <p className="text-sm text-slate-400">Everything is adequately stocked.</p>}
        </div>
      </section>

      <section className="grid gap-6 lg:grid-cols-2">
        <article className="rounded-3xl border border-white/10 bg-white/5 p-6 text-sm text-slate-200">
          <p className="text-xs uppercase tracking-[0.4em] text-slate-400">About cost of goods</p>
          <p className="mt-4">
            FIFO allocations ensure that COGS reflects historical purchase rates. The analytics endpoint exposes those
            numbers so you can surface them to finance dashboards or stores.
          </p>
        </article>
        <article className="rounded-3xl border border-white/10 bg-white/5 p-6 text-sm text-slate-200">
          <p className="text-xs uppercase tracking-[0.4em] text-slate-400">Next steps</p>
          <ul className="mt-4 space-y-2 text-slate-300">
            <li>• Alert when GST output exceeds inputs.</li>
            <li>• Render detailed stock history per SKU.</li>
            <li>• Tie analytics cards into live websocket streams later.</li>
          </ul>
        </article>
      </section>
    </main>
  );
}
