import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-950 text-slate-100">
        <Sidebar />
        <div className="ml-0 flex min-h-screen flex-1 flex-col lg:ml-64">
          <Navbar />
          <main className="flex-1 bg-slate-950/70 p-6 lg:p-10">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
