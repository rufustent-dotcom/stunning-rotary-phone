import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Rotary Phone World",
  description: "An interactive rotary phone dial experience",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
