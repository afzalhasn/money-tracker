import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./hooks/**/*.{ts,tsx}",
    "./services/**/*.{ts,tsx}",
  ],
  theme: {
    fontFamily: {
      sans: ["var(--font-sans)", "Inter", "system-ui", "sans-serif"],
      mono: ["var(--font-mono)", "SFMono-Regular", "ui-monospace", "monospace"],
    },
    extend: {
      colors: {
        background: "var(--color-background)",
        surface: "var(--color-surface)",
        primary: "var(--color-primary)",
        primaryForeground: "var(--color-primary-foreground)",
        danger: "var(--color-danger)",
        border: "var(--color-border)",
        muted: "var(--color-muted)",
        text: "var(--color-text)",
      },
      borderRadius: {
        DEFAULT: "var(--radius-base)",
        lg: "calc(var(--radius-base) * 1.25)",
      },
      spacing: {
        xs: "0.5rem",
        sm: "0.75rem",
        md: "1.25rem",
        lg: "2rem",
      },
      boxShadow: {
        soft: "var(--shadow-soft)",
      },
    },
  },
  plugins: [],
};

export default config;
