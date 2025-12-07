"use client";

import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { PageContainer } from "@/components/layout/PageContainer";
import { SectionHeader } from "@/components/layout/SectionHeader";

const inventoryStats = [
  { label: "Total SKUs", value: "128", caption: "across categories" },
  { label: "Low stock", value: "7", caption: "needs restock alerts" },
  { label: "Avg. cost", value: "$42.8", caption: "from FIFO batches" },
];

const sampleItems = [
  { name: "Widget Alpha", sku: "WA-001", stock: 18, price: "$120.00" },
  { name: "Widget Beta", sku: "WB-005", stock: 6, price: "$85.00" },
  { name: "Parts X12", sku: "PX-110", stock: 42, price: "$23.50" },
];

export default function ItemsPage() {
  return (
    <PageContainer>
      <SectionHeader
        title="Items"
        subtitle="Catalog, stock, and pricing summary"
        actions={
          <Button variant="ghost">
            <span className="uppercase tracking-[0.3em]">Exports</span>
          </Button>
        }
      />

      <div className="grid gap-5 md:grid-cols-3">
        {inventoryStats.map((stat) => (
          <Card key={stat.label}>
            <p className="text-xs uppercase tracking-[0.4em] text-slate-400">{stat.label}</p>
            <p className="mt-2 text-3xl font-semibold text-white">{stat.value}</p>
            <p className="text-sm text-slate-400">{stat.caption}</p>
          </Card>
        ))}
      </div>

      <div className="mt-8 grid gap-6 lg:grid-cols-[1.2fr_1fr]">
        <Card title="Add new item">
          <form className="space-y-4">
            <Input label="Name" placeholder="New SKU name" />
            <Input label="SKU" placeholder="EX123" />
            <Input label="Unit price" placeholder="$0.00" />
            <div className="flex justify-end">
              <Button type="button">Save</Button>
            </div>
          </form>
        </Card>

        <Card title="Legend">
          <p className="mb-3 text-sm text-slate-400">
            Items pages will eventually load catalog data from TanStack Query services while reusing this consistent form/table layout.
          </p>
          <div className="space-y-3">
            <p className="text-xs uppercase tracking-[0.3em] text-slate-400">Highlights</p>
            <ul className="space-y-2 text-sm text-slate-300">
              <li>• Shared layout components keep spacing predictable.</li>
              <li>• Themed inputs + buttons align with the design system.</li>
              <li>• Lists should show real-time inventory metadata later.</li>
            </ul>
          </div>
        </Card>
      </div>

      <Card className="mt-8" title="Catalog">
        <div className="overflow-hidden rounded-3xl border border-border">
          <table className="min-w-full divide-y divide-white/5 text-left">
            <thead>
              <tr className="bg-slate-950">
                <th className="px-6 py-3 text-xs uppercase tracking-[0.3em] text-slate-400">Name</th>
                <th className="px-6 py-3 text-xs uppercase tracking-[0.3em] text-slate-400">SKU</th>
                <th className="px-6 py-3 text-xs uppercase tracking-[0.3em] text-slate-400">Stock</th>
                <th className="px-6 py-3 text-xs uppercase tracking-[0.3em] text-slate-400">Unit price</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5 bg-slate-900">
              {sampleItems.map((item) => (
                <tr key={item.sku} className="transition hover:bg-slate-800/70">
                  <td className="px-6 py-4 text-sm font-semibold text-white">{item.name}</td>
                  <td className="px-6 py-4 text-sm text-slate-300">{item.sku}</td>
                  <td className="px-6 py-4 text-sm text-slate-300">{item.stock}</td>
                  <td className="px-6 py-4 text-sm text-primary">{item.price}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>
    </PageContainer>
  );
}
