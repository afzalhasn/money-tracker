"use client";

import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Chart } from "@/components/ui/Chart";
import { PageContainer } from "@/components/layout/PageContainer";
import { SectionHeader } from "@/components/layout/SectionHeader";

const statHighlights = [
  { label: "Live Stories", value: "08", detail: "Phase A/B verified" },
  { label: "Design Tokens", value: "26", detail: "Color + typography units" },
  { label: "API Routing", value: "12", detail: "Endpoints mapped for Phase G" },
];

const timeline = [
  { phase: "Phase C", summary: "UI foundation, globals, design tokens", status: "✅" },
  { phase: "Phase D", summary: "Layout shell + navigation", status: "✅" },
  { phase: "Phase E", summary: "Dashboard + analytics mock", status: "✅" },
  { phase: "Phase F", summary: "Feature pages (mock first)", status: "In progress" },
];

const focusAreas = [
  "Reusable components (Card, Chart, Button, Skeleton)",
  "Consistent PageContainer + SectionHeader layouts",
  "Mock-first data in Items, Dashboard, upcoming Purchases/Sales",
  "TanStack Query + services planning for Phase G",
];

const chartData = [24, 32, 39, 35, 44, 50, 60, 58, 68, 72];

export default function Home() {
  return (
    <PageContainer className="space-y-10 pb-16">
      <section className="grid gap-6 lg:grid-cols-[1.4fr_0.6fr]">
        <Card className="relative overflow-hidden bg-gradient-to-br from-primary/70 via-primary/60 to-slate-950/80 text-white">
          <div className="space-y-6">
            <p className="text-xs uppercase tracking-[0.4em] text-white/70">Money Tracker</p>
            <div>
              <h1 className="text-4xl font-semibold leading-tight md:text-5xl">
                Beautiful screens, disciplined finance
              </h1>
              <p className="mt-3 max-w-2xl text-base text-white/80">
                Phase by phase we are shaping a Next.js + FastAPI system—mocked dashboards tie into real
                analytics, shared components keep the UI clean, and the upcoming services will wire every
                API route to a polished page.
              </p>
            </div>
            <div className="flex flex-wrap gap-3">
              <Button>Open dashboard</Button>
              <Button variant="ghost" size="sm">
                View roadmap
              </Button>
            </div>
            <div className="grid gap-4 sm:grid-cols-3">
              {statHighlights.map((stat) => (
                <div key={stat.label} className="rounded-2xl border border-white/20 bg-white/5 p-4">
                  <p className="text-xs uppercase tracking-[0.3em] text-white/60">{stat.label}</p>
                  <p className="mt-1 text-3xl font-semibold">{stat.value}</p>
                  <p className="text-xs text-white/60">{stat.detail}</p>
                </div>
              ))}
            </div>
          </div>
          <div
            aria-hidden
            className="pointer-events-none absolute inset-0 opacity-60"
            style={{
              background:
                "radial-gradient(circle at top right, rgba(239, 68, 68, 0.35), transparent 45%), radial-gradient(circle at bottom left, rgba(14, 165, 233, 0.35), transparent 45%)",
            }}
          />
        </Card>

        <Card>
          <SectionHeader title="Phase status" subtitle="UI-first progress" />
          <div className="mt-4 space-y-4">
            {timeline.map((step) => (
              <div
                key={step.phase}
                className="flex items-center justify-between gap-4 rounded-2xl border border-border bg-slate-950/40 p-4"
              >
                <div>
                  <p className="text-sm font-semibold text-white">{step.phase}</p>
                  <p className="text-xs text-slate-400">{step.summary}</p>
                </div>
                <span
                  className={`rounded-full px-3 py-1 text-xs font-semibold ${
                    step.status === "In progress"
                      ? "bg-primary/10 text-primary"
                      : "bg-emerald-500/15 text-emerald-300"
                  }`}
                >
                  {step.status}
                </span>
              </div>
            ))}
          </div>
        </Card>
      </section>

      <section className="space-y-6">
        <SectionHeader title="Design rhythm" subtitle="Mocked data now, services soon" />
        <div className="grid gap-6 lg:grid-cols-[1.6fr_1fr]">
          <Card title="Momentum tracker">
            <Chart data={chartData} height={150} />
            <p className="mt-4 text-sm text-slate-400">
              Mock activity for the Phase E/F components—this sparkline reflects how component coverage grew.
            </p>
          </Card>
          <Card title="Focus for Phase F">
            <ul className="space-y-3 text-sm text-slate-200">
              {focusAreas.map((focus) => (
                <li key={focus} className="flex items-start gap-2">
                  <span className="mt-1 h-2 w-2 rounded-full bg-primary" />
                  <span>{focus}</span>
                </li>
              ))}
            </ul>
          </Card>
        </div>
      </section>

      <section className="space-y-4">
        <SectionHeader title="What’s next" subtitle="Keep the UI consistent then wire endpoints" />
        <div className="grid gap-5 md:grid-cols-3">
          <Card title="Items & docs">
            <p className="text-sm text-slate-300">
              Mock grids already display the data, now we prepare the TanStack Query services to fetch the real
              records.
            </p>
          </Card>
          <Card title="Purchases & sales">
            <p className="text-sm text-slate-300">
              Phase F continues with buy/sell flow pages—reuse layout components, match spacing, keep typography
              tokens consistent.
            </p>
          </Card>
          <Card title="GST & analytics">
            <p className="text-sm text-slate-300">
              Stakes are reporting accuracy, so the polished UI now serves as the canvas for later data hookups.
            </p>
          </Card>
        </div>
      </section>
    </PageContainer>
  );
}
