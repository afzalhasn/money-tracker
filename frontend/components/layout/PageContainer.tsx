"use client";

import type { ReactNode } from "react";

export type PageContainerProps = {
  children: ReactNode;
  className?: string;
};

export function PageContainer({ children, className = "" }: PageContainerProps) {
  return (
    <section className={`mx-auto max-w-6xl space-y-6 px-4 py-10 sm:px-6 lg:px-8 ${className}`}>
      {children}
    </section>
  );
}
