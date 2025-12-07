interface CardProps {
  title: string;
  value: string;
  caption?: string;
  trend?: string;
  accent?: string;
}

export default function Card({ title, value, caption, trend, accent = "from-teal-400 to-blue-600" }: CardProps) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/80 p-6 shadow-lg shadow-slate-900/10 backdrop-blur">
      <div className="flex items-center justify-between text-xs uppercase tracking-widest text-slate-500">
        <span>{title}</span>
        {trend && <span className="font-semibold text-slate-400">{trend}</span>}
      </div>
      <div className="mt-4 flex items-baseline gap-2 text-3xl font-bold text-slate-900">
        <span className="text-4xl">{value}</span>
      </div>
      {caption && <p className="mt-3 text-sm text-slate-500">{caption}</p>}
    </div>
  );
}
