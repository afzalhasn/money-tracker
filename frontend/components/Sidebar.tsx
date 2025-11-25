"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Sidebar() {
  const pathname = usePathname() || "/";
  const [collapsed, setCollapsed] = useState(false);

  const links = [
    { href: "/dashboard", label: "Dashboard" },
    { href: "/items", label: "Items" },
    { href: "/purchases", label: "Purchases" },
    { href: "/sales", label: "Sales" },
    { href: "/expenses", label: "Expenses" },
    { href: "/investments", label: "Investments" },
    { href: "/documents", label: "Documents" },
    { href: "/analytics", label: "Analytics" },
  ];

  return (
    <aside
      className={`h-screen sticky top-0 bg-white border-r border-gray-200 p-4 transition-all duration-200 ${
        collapsed ? "w-16" : "w-64"
      }`}
    >
      <div className="flex items-center justify-between mb-6">
        <h1 className={`text-lg font-semibold ${collapsed ? "hidden" : "block"}`}>
          Money Tracker
        </h1>
        <button
          aria-label="Toggle sidebar"
          onClick={() => setCollapsed((s) => !s)}
          className="p-1 rounded hover:bg-gray-100"
        >
          {collapsed ? "→" : "←"}
        </button>
      </div>

      <nav className="flex flex-col gap-1">
        {links.map((l) => {
          const active = pathname === l.href || pathname.startsWith(l.href + "/");
          return (
            <Link
              key={l.href}
              href={l.href}
              className={`flex items-center gap-3 p-2 rounded-md text-sm hover:bg-gray-100 transition-colors ${
                active ? "bg-gray-100 font-semibold" : ""
              }`}
            >
              <span className="w-6 text-center">{l.label.charAt(0)}</span>
              {!collapsed && <span>{l.label}</span>}
            </Link>
          );
        })}
      </nav>

      <div className="mt-auto pt-6">
        <div className="text-xs text-gray-500">v1.0.0</div>
        {!collapsed && <div className="text-xs text-gray-400 mt-1">Logged in as: Staff</div>}
      </div>
    </aside>
  );
}
