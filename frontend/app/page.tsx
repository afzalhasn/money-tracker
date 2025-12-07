"use client";

import Card from "@/components/Card";
import Chart from "@/components/Chart";

const stats = [
  {
    title: "Revenue",
    value: "$124.3K",
    trend: "+14% vs last month",
    caption: "Bookings cleared through Phase A APIs",
  },
  {
    title: "COGS",
    value: "$58.1K",
    trend: "—3% vs last month",
    caption: "FIFO engine keeps the cost base tight",
  },
  {
    title: "GST Offset",
    value: "$9.4K",
    trend: "+6% pending return",
    caption: "Ledger captures inputs & outputs",
  },
];

const sparkData = [38, 45, 52, 48, 62, 72, 80, 74];

export default function Home() {
  return (
    <div className="flex min-h-screen w-full flex-col gap-12 bg-slate-50 p-8 text-slate-900">
      <section className="grid gap-10 rounded-3xl bg-gradient-to-br from-slate-800 via-slate-900 to-slate-950 p-10 shadow-2xl text-white md:grid-cols-[1.5fr_1fr]">
        <div className="space-y-6">
          <p className="text-xs uppercase tracking-[0.3em] text-slate-200">Money Tracker</p>
          <h1 className="text-4xl font-semibold leading-tight text-white sm:text-5xl">
            Fast insights, confident decisions.
          </h1>
          <p className="max-w-2xl text-base text-slate-200">
            Connect purchases, sales, and GST through a single API layer and explore chart-ready summaries in
            seconds. Power a beautiful dashboard front end with consistent widgets and friendly navigation.
          </p>
          <div className="flex flex-wrap gap-3">
            <button className="rounded-full bg-white px-6 py-3 text-sm font-semibold uppercase tracking-wider text-slate-800 shadow-lg shadow-black/20 transition hover:bg-slate-100">
              Explore analytics
            </button>
            <button className="rounded-full border border-white/30 px-6 py-3 text-sm font-semibold uppercase tracking-wider text-white transition hover:border-white">
              View API docs
            </button>
          </div>
        </div>
        <div className="space-y-4 rounded-3xl bg-white/10 p-6 backdrop-blur">
          <div className="flex items-center justify-between text-sm text-slate-200">
            <span>Results widget</span>
            <span className="text-xs">Updated just now</span>
          </div>
          <div className="text-3xl font-semibold text-white">
            +18.4% <span className="text-sm font-medium text-slate-200">growth</span>
          </div>
          <p className="text-sm text-slate-300">Bookings aligned with FIFO allocations and GST ledger checks.</p>
          <Chart data={sparkData} />
          <div className="text-xs uppercase tracking-widest text-slate-300">Revenue vs target</div>
        </div>
      </section>

      <section className="grid gap-6 md:grid-cols-3">
        {stats.map((stat) => (
          <Card key={stat.title} {...stat} />
        ))}
      </section>
    </div>
  );
}
