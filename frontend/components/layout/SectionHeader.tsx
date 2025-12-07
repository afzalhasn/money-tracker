"use client";

import type { ReactNode } from "react";

export type SectionHeaderProps = {
  title: string;
  subtitle?: string;
  actions?: ReactNode;
};

export function SectionHeader({ title, subtitle, actions }: SectionHeaderProps) {
  return (
    <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
      <div>
        <p className="text-xs uppercase tracking-[0.4em] text-slate-400">{title}</p>
        {subtitle && <p className="text-sm text-slate-300">{subtitle}</p>}
      </div>
      {actions && <div className="flex items-center gap-2">{actions}</div>}
    </div>
  );
}
