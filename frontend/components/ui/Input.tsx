"use client";

import type { InputHTMLAttributes } from "react";

export type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label?: string;
  helperText?: string;
};

export function Input({ label, helperText, className = "", ...props }: InputProps) {
  return (
    <label className="flex flex-col gap-2 text-sm capitalize text-slate-200">
      {label && <span className="text-xs uppercase tracking-[0.3em] text-slate-400">{label}</span>}
      <input
        className={`rounded-2xl border border-border bg-slate-950/40 px-4 py-3 text-sm text-white transition focus:border-primary focus:outline-none ${className}`}
        {...props}
      />
      {helperText && <span className="text-[0.6rem] text-slate-400">{helperText}</span>}
    </label>
  );
}
