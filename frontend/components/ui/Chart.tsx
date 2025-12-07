"use client";

type ChartProps = {
  data: number[];
  height?: number;
  className?: string;
};

export function Chart({ data, height = 140, className = "" }: ChartProps) {
  if (!data.length) {
    return (
      <div
        className={`rounded-2xl border border-border bg-gradient-to-br from-white/10 to-white/5 ${className}`}
        style={{ height }}
      />
    );
  }

  const max = Math.max(...data);
  const min = Math.min(...data);
  const range = max - min || 1;

  const points = data
    .map((value, index) => {
      const x = (index / (data.length - 1 || 1)) * 100;
      const y = 100 - ((value - min) / range) * 100;
      return `${x},${y}`;
    })
    .join(" ");

  return (
    <svg
      aria-hidden
      viewBox="0 0 100 100"
      className={`w-full rounded-2xl border border-border bg-gradient-to-br from-white/10 to-white/5 p-2 ${className}`}
      style={{ height }}
    >
      <defs>
        <linearGradient id="chartGradient" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#a5b4fc" />
          <stop offset="70%" stopColor="#38bdf8" />
        </linearGradient>
      </defs>
      <polyline
        points={points}
        fill="none"
        stroke="url(#chartGradient)"
        strokeWidth="2.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
