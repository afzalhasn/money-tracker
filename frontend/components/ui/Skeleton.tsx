"use client";

import type { ReactNode } from "react";

export type SkeletonProps = {
  width?: string;
  height?: string;
  children?: ReactNode;
};

export function Skeleton({ width = "100%", height = "1rem" }: SkeletonProps) {
  return (
    <div
      aria-hidden="true"
      className="animate-pulse rounded-2xl border border-white/10 bg-gradient-to-r from-white/5 via-white/10 to-white/5"
      style={{ width, height }}
    />
  );
}
