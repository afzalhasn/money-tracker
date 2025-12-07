"use client";

import { useEffect } from "react";
import type { ReactNode } from "react";

export type DialogProps = {
  open: boolean;
  onClose: () => void;
  title?: string;
  children: ReactNode;
};

export function Dialog({ open, onClose, title, children }: DialogProps) {
  useEffect(() => {
    if (!open) return;
    const handle = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        onClose();
      }
    };
    window.addEventListener("keydown", handle);
    return () => window.removeEventListener("keydown", handle);
  }, [open, onClose]);

  if (!open) {
    return null;
  }

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/80"
      role="dialog"
      aria-modal="true"
    >
      <div className="relative max-w-lg rounded-3xl border border-border bg-slate-950/80 p-6 shadow-soft">
        <button
          className="absolute right-4 top-4 text-sm text-slate-400 hover:text-white"
          onClick={onClose}
          aria-label="Close dialog"
        >
          ×
        </button>
        {title && <h2 className="text-lg font-semibold">{title}</h2>}
        <div className="mt-4 space-y-4">{children}</div>
      </div>
    </div>
  );
}
