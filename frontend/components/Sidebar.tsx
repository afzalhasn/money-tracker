"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useMemo, useState } from "react";

const Icon = ({ path }: { path: string }) => (
  <svg
    className="h-5 w-5"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="1.5"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d={path} />
  </svg>
);

const links = [
  { href: "/dashboard", label: "Dashboard", icon: "M3 12h18M3 6h18M3 18h18" },
  { href: "/items", label: "Items", icon: "M4 6h16v12H4z" },
  { href: "/purchases", label: "Purchases", icon: "M6 9l3 3-3 3" },
  { href: "/sales", label: "Sales", icon: "M17 4H7v16h10V4z" },
  { href: "/expenses", label: "Expenses", icon: "M6 4h12v4H6zM6 12h12v4H6z" },
  { href: "/investments", label: "Investments", icon: "M4 17l4-4 4 4 4-6 4 6" },
  { href: "/documents", label: "Documents", icon: "M6 2h7l5 5v13H6z" },
  { href: "/analytics", label: "Analytics", icon: "M4 16h4v4H4zM10 10h4v10h-4zM16 4h4v16h-4z" },
];

export default function Sidebar() {
  const pathname = usePathname() || "/";
  const [collapsed, setCollapsed] = useState(false);

  const activeLink = useMemo(
    () => links.find((link) => pathname === link.href || pathname.startsWith(link.href + "/")),
    [pathname]
  );

  return (
    <aside
      className={`fixed inset-y-0 left-0 z-30 flex w-full flex-col border-r border-border bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 px-4 py-6 text-sm text-slate-300 shadow-2xl backdrop-blur lg:relative lg:w-64 ${
        collapsed ? "lg:w-20" : "lg:w-64"
      }`}
    >
      <div className="flex items-center justify-between pb-6">
        {!collapsed && (
          <div>
            <p className="text-xs uppercase tracking-[0.4em] text-slate-400">Money Tracker</p>
            <p className="text-xl font-semibold text-white">Operations</p>
          </div>
        )}
        <button
          onClick={() => setCollapsed((prev) => !prev)}
          className="rounded-full border border-white/10 bg-white/5 p-2 text-xs text-slate-100 transition hover:border-white"
          aria-label="Toggle sidebar"
        >
          {collapsed ? "→" : "←"}
        </button>
      </div>

      <nav className="flex flex-1 flex-col gap-2">
        {links.map((link) => {
          const active = activeLink?.href === link.href;
          return (
            <Link
              key={link.href}
              href={link.href}
              className={`flex items-center gap-3 rounded-2xl px-3 py-2 transition hover:bg-slate-900/80 ${
                active ? "bg-primary/90 text-primaryForeground" : "bg-white/5"
              } ${collapsed ? "justify-center" : ""}`}
            >
              <Icon path={link.icon} />
              {!collapsed && <span className="text-sm font-semibold">{link.label}</span>}
            </Link>
          );
        })}
      </nav>

      <div className="mt-6 border-t border-white/5 pt-4 text-xs text-slate-500">
        <p>v1.0.0</p>
        {!collapsed && <p className="text-slate-400">Logged in as Staff</p>}
      </div>
    </aside>
  );
}
