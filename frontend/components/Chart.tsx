interface ChartProps {
  data: number[];
  color?: string;
}

export default function Chart({ data, color = "#2563eb" }: ChartProps) {
  if (data.length === 0) {
    return <div className="h-24 rounded-2xl bg-slate-100" aria-hidden />;
  }

  const max = Math.max(...data);
  const normalized = data.map((value, index) => {
    const x = (index / (data.length - 1 || 1)) * 100;
    const y = 100 - (value / (max || 1)) * 100;
    return `${x},${y}`;
  });

  const polylinePoints = normalized.join(" ");

  const areaPoints = `${normalized[0]} ${normalized
    .slice(1)
    .join(" ")} ${100},100 0,100`;

  return (
    <svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden className="h-32 w-full">
      <defs>
        <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor={color} stopOpacity="0.35" />
          <stop offset="100%" stopColor={color} stopOpacity="0" />
        </linearGradient>
      </defs>
      <path d={`M${areaPoints}`} fill="url(#areaGradient)" />
      <polyline
        points={polylinePoints}
        fill="none"
        stroke={color}
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
