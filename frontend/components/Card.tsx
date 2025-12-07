interface CardProps {
  title: string;
  value: string;
  caption?: string;
  trend?: string;
  accent?: string;
}

export default function Card({
  title,
  value,
  caption,
  trend,
  accent = "from-indigo-500/80 to-sky-500/70",
}: CardProps) {
  return (
    <div className="flex flex-col rounded-3xl border border-white/20 bg-gradient-to-br from-white/70 via-white/30 to-white/10 p-6 shadow-2xl shadow-slate-900/40 backdrop-blur">
      <div className={`h-1 w-16 rounded-full bg-gradient-to-r ${accent}`} aria-hidden />
      <div className="mt-3 flex items-center justify-between text-[0.6rem] uppercase tracking-[0.4em] text-slate-500">
        <span>{title}</span>
        {trend && <span className="font-semibold text-slate-400">{trend}</span>}
      </div>
      <div className="mt-3 text-4xl font-semibold text-slate-900">{value}</div>
      {caption && <p className="mt-2 text-sm text-slate-500">{caption}</p>}
    </div>
  );
}
