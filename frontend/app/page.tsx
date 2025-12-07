"use client";

import Card from "@/components/Card";
import Chart from "@/components/Chart";
import FeatureTile from "@/components/FeatureTile";
import Link from "next/link";

const heroStats = [
  { label: "Active SKUs", value: "128", subtext: "inventory tracked" },
  { label: "FIFO Batches", value: "452", subtext: "freshly aligned" },
  { label: "GST Entries", value: "1.2K", subtext: "reconciled" },
];

const resultCards = [
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

const features = [
  {
    title: "Unified Inventory",
    description: "Track purchases, batches, and current stock with one API surface and keep FIFO integrity.",
  },
  {
    title: "Autonomous GST",
    description: "Ledger writes for every purchase or sale, letting you export summaries quickly for compliance.",
  },
  {
    title: "Analytics Ready",
    description: "Profit and stock endpoints feed dashboards with confidence, ready for the UI widgets you design.",
  },
];

export default function Home() {
  return (
    <div className="flex min-h-screen w-full flex-col gap-14 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-900 px-8 py-10 text-white">
      <section className="grid gap-10 rounded-[32px] bg-white/5 p-10 shadow-2xl shadow-black/40 backdrop-blur-xl md:grid-cols-[1.4fr_1fr]">
        <div className="space-y-6">
          <p className="text-xs uppercase tracking-[0.4em] text-slate-300">Money Tracker</p>
          <h1 className="text-4xl font-semibold leading-tight md:text-5xl">
            Make every ledger entry feel like a well-designed product card.
          </h1>
          <p className="max-w-2xl text-base text-slate-200">
            Connect inventory, purchases, sales, and GST through FastAPI while the Next.js frontend renders results driven UI without extra coordination.
          </p>
          <div className="flex flex-wrap gap-3">
            <Link
              href="/analytics"
              className="rounded-full bg-white px-6 py-3 text-xs font-semibold uppercase tracking-[0.4em] text-slate-900 shadow-lg shadow-black/40 transition hover:bg-slate-100"
            >
              Explore analytics
            </Link>
            <Link
              href="/docs"
              className="rounded-full border border-white/40 px-6 py-3 text-xs font-semibold uppercase tracking-[0.4em] text-white transition hover:border-white"
            >
              View API docs
            </Link>
          </div>
          <div className="grid gap-4 text-sm text-slate-300 sm:grid-cols-3">
            {heroStats.map((stat) => (
              <div key={stat.label} className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur">
                <p className="text-xs uppercase tracking-[0.3em] text-slate-400">{stat.label}</p>
                <p className="text-2xl font-semibold text-white">{stat.value}</p>
                <p className="text-xs text-slate-200">{stat.subtext}</p>
              </div>
            ))}
          </div>
        </div>
        <div className="space-y-6 rounded-[28px] border border-white/10 bg-slate-900/60 p-6 backdrop-blur-xl">
          <div className="flex items-center justify-between text-xs uppercase tracking-[0.4em] text-slate-400">
            <span>Results widget</span>
            <span className="text-[0.6rem]">Synced just now</span>
          </div>
          <div className="text-3xl font-bold text-white">
            +18.4% <span className="text-xs font-medium text-slate-300">growth</span>
          </div>
          <p className="text-sm text-slate-300">Every sale stays FIFO clean, every GST entry balanced.</p>
          <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
            <Chart data={sparkData} className="rounded-xl" />
          </div>
          <div className="text-xs uppercase tracking-[0.4em] text-slate-400">Revenue vs target</div>
        </div>
      </section>

      <section className="grid gap-6 md:grid-cols-3">
        {resultCards.map((card) => (
          <Card key={card.title} {...card} />
        ))}
      </section>

      <section className="space-y-6">
        <div className="flex flex-col gap-2">
          <p className="text-xs uppercase tracking-[0.4em] text-slate-300">Built for ops teams</p>
          <h2 className="text-3xl font-semibold">Fresh widgets inspired by UntitledUI aesthetics</h2>
          <p className="max-w-3xl text-base text-slate-300">
            Combine high-contrast hero text, layered gradients, and crisp typography to create dashboards that feel alive. The FastAPI backend stays lean while the UI layers deliver the “good widget” promise.
          </p>
        </div>
        <div className="grid gap-5 md:grid-cols-3">
          {features.map((feature) => (
            <FeatureTile key={feature.title} title={feature.title} description={feature.description} accent="bg-gradient-to-br from-slate-700 to-slate-900/70" />
          ))}
        </div>
      </section>
    </div>
  );
}
