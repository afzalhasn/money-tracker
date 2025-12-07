"use client";

import Link from "next/link";
import { Button } from "@/components/ui/Button";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 flex w-full items-center justify-between gap-6 border-b border-border bg-slate-950/70 px-6 py-4 backdrop-blur">
      <div className="flex items-center gap-3">
        <span className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-primaryForeground text-2xl font-semibold text-slate-950 shadow-soft">
          MT
        </span>
        <div>
          <p className="text-xs uppercase tracking-[0.4em] text-slate-400">Money Tracker</p>
          <p className="text-lg font-semibold text-white">Reporting & Inventory</p>
        </div>
      </div>
      <div className="flex items-center gap-3">
        <Link
          href="/analytics"
          className="text-xs font-medium uppercase tracking-[0.3em] text-slate-300 transition hover:text-white"
        >
          Analytics
        </Link>
        <Button variant="ghost" size="md">
          Feedback
        </Button>
      </div>
    </header>
  );
}
