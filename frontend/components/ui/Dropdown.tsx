"use client";

import { useRef, useState } from "react";
import type { ReactNode } from "react";

export type DropdownItem = {
  label: string;
  onSelect: () => void;
};

export type DropdownProps = {
  triggerLabel: string;
  items: DropdownItem[];
};

export function Dropdown({ triggerLabel, items }: DropdownProps) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLButtonElement>(null);

  return (
    <div className="relative inline-flex">
      <button
        ref={ref}
        onClick={() => setOpen((prev) => !prev)}
        className="rounded-2xl border border-border bg-slate-900/70 px-4 py-2 text-sm font-semibold uppercase tracking-[0.3em]"
      >
        {triggerLabel}
      </button>
      {open && (
        <div className="absolute right-0 mt-2 w-48 rounded-2xl border border-border bg-slate-950/90 p-2 shadow-soft">
          {items.map((item) => (
            <button
              key={item.label}
              onClick={() => {
                item.onSelect();
                setOpen(false);
              }}
              className="block w-full rounded-xl px-3 py-2 text-left text-sm text-slate-200 transition hover:bg-slate-800"
            >
              {item.label}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
