"use client";

import type { ReactNode } from "react";

export type CardProps = {
  title?: string;
  children: ReactNode;
  className?: string;
  footer?: ReactNode;
};

export function Card({ title, children, footer, className = "" }: CardProps) {
  return (
    <div
      className={`rounded-[32px] border border-border bg-slate-900/70 p-6 shadow-soft backdrop-blur ${className}`}
    >
      {title && <h3 className="text-sm uppercase tracking-[0.3em] text-slate-400">{title}</h3>}
      <div className="mt-4">{children}</div>
      {footer && <div className="mt-6 text-xs text-slate-400">{footer}</div>}
    </div>
  );
}
