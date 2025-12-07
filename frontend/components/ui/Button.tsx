import type { ButtonHTMLAttributes } from "react";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "ghost";
  size?: "sm" | "md";
};

const variantStyles: Record<ButtonProps["variant"], string> = {
  primary: "bg-primary text-primaryForeground shadow-soft border border-transparent",
  ghost: "bg-white/10 text-primary border border-white/20",
};

const sizeStyles: Record<ButtonProps["size"], string> = {
  sm: "px-3 py-2 text-sm",
  md: "px-5 py-3 text-base",
};

export function Button({
  variant = "primary",
  size = "md",
  className = "",
  ...props
}: ButtonProps) {
  const classes = [
    "rounded-2xl font-semibold uppercase tracking-[0.1em] transition hover:brightness-110 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary",
    variantStyles[variant],
    sizeStyles[size],
    className,
  ]
    .filter(Boolean)
    .join(" ");
  return <button className={classes} {...props} />;
}
