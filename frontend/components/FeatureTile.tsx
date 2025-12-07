interface FeatureTileProps {
  title: string;
  description: string;
  accent?: string;
}

export default function FeatureTile({ title, description, accent = "bg-white/30" }: FeatureTileProps) {
  return (
    <div className={`flex h-full flex-col gap-3 rounded-2xl border border-white/20 bg-slate-900/60 p-6 text-white backdrop-blur ${accent}`}>
      <p className="text-sm uppercase tracking-[0.4em] text-white/70">Feature</p>
      <h3 className="text-xl font-semibold">{title}</h3>
      <p className="text-sm text-white/80">{description}</p>
    </div>
  );
}
