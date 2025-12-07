"use client";

import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Chart } from "@/components/ui/Chart";
import { PageContainer } from "@/components/layout/PageContainer";
import { SectionHeader } from "@/components/layout/SectionHeader";
import { Skeleton } from "@/components/ui/Skeleton";

const stats = [
  { title: "Revenue", value: "$124.3K", caption: "+14% vs last month" },
  { title: "COGS", value: "$58.1K", caption: "FIFO stabilized" },
  { title: "GST Offset", value: "$9.4K", caption: "Input > output" },
];

const chartData = [28, 35, 42, 37, 50, 61, 58, 70, 74, 68];

const transactions = [
  { label: "Sales", value: "+$34.1K", detail: "5 invoices processed" },
  { label: "Purchases", value: "-$12.8K", detail: "3 suppliers delivered" },
  { label: "Stock Value", value: "$82.9K", detail: "FIFO-aligned balance" },
];

export default function DashboardPage() {
  const loading = false;

  return (
    <PageContainer>
      <SectionHeader
        title="Dashboard"
        subtitle="Design-first analytics wireframe"
        actions={
          <Button variant="ghost">
            <span className="uppercase tracking-[0.3em]">Export</span>
          </Button>
        }
      />

      <div className="grid gap-6 md:grid-cols-3">
        {loading
          ? Array.from({ length: 3 }).map((_, index) => (
              <Skeleton key={index} width="100%" height="120px" />
            ))
          : stats.map((stat) => (
              <Card key={stat.title}>
                <p className="text-xs uppercase tracking-[0.4em] text-slate-400">{stat.title}</p>
                <p className="mt-2 text-4xl font-semibold text-white">{stat.value}</p>
                <p className="text-sm text-slate-400">{stat.caption}</p>
              </Card>
            ))}
      </div>

      <section className="mt-8 grid gap-6 lg:grid-cols-[1.6fr_1fr]">
        <Card title="Revenue Trend">
          <Chart data={chartData} height={150} />
          <p className="mt-3 text-sm text-slate-400">Mock data only — the backend integration comes later.</p>
        </Card>

        <Card title="Snapshot">
          <div className="space-y-4">
            {transactions.map((txn) => (
              <div key={txn.label} className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-semibold text-white">{txn.label}</p>
                  <p className="text-xs text-slate-400">{txn.detail}</p>
                </div>
                <p className="text-sm font-semibold text-primary">{txn.value}</p>
              </div>
            ))}
          </div>
          <div className="mt-6 flex items-center justify-between text-xs text-slate-500">
            <span>Updated just now</span>
            <Button variant="ghost" size="sm">
              Refresh
            </Button>
          </div>
        </Card>
      </section>
    </PageContainer>
  );
}
