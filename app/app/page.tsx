"use client";

import { useState } from "react";

const HOLES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

const FACTS = [
  "The rotary phone was invented in the late 19th century.",
  "Rotary dials were standard in homes from the 1920s through the 1970s.",
  "Each digit on the dial corresponds to a specific number of pulses sent down the line.",
  "Dialing '0' sends 10 pulses — the longest pause of any digit.",
  "The finger stop (a small metal tab) prevents over-rotation.",
  "Rotary phones used pulse dialing, unlike modern touch-tone (DTMF) phones.",
  "AT&T introduced the first commercial touch-tone service in 1963, gradually replacing rotary.",
  "Many classic film noir movies feature the iconic sound of a rotary dial.",
  "Rotary phones are still manufactured today as retro collectibles.",
  "The word 'dial' in 'dial a number' comes directly from rotary phone dials.",
];

export default function Home() {
  const [dialed, setDialed] = useState<number[]>([]);
  const [spinning, setSpinning] = useState<number | null>(null);
  const [factIndex, setFactIndex] = useState(0);

  function handleDial(digit: number) {
    if (spinning !== null) return;
    setSpinning(digit);
    setDialed((prev) => [...prev.slice(-6), digit]);
    // Show the fact that corresponds to the dialed digit (0 maps to index 9)
    setFactIndex(digit === 0 ? 9 : digit - 1);
    setTimeout(() => setSpinning(null), 600);
  }

  function handleClear() {
    setDialed([]);
  }

  return (
    <main className="min-h-screen bg-amber-50 flex flex-col items-center justify-center px-4 py-12">
      <h1 className="text-4xl font-bold text-amber-900 mb-2 tracking-tight">
        ☎ Rotary Phone World
      </h1>
      <p className="text-amber-700 mb-8 text-center max-w-md">
        Click a digit to spin the dial. Hear the satisfying click of a bygone era.
      </p>

      {/* Phone body */}
      <div className="relative bg-neutral-800 rounded-3xl shadow-2xl p-8 flex flex-col items-center w-72">
        {/* Display */}
        <div className="w-full bg-neutral-900 rounded-xl mb-6 px-4 py-2 flex items-center justify-between min-h-[2.5rem]">
          <span className="text-green-400 font-mono text-xl tracking-widest">
            {dialed.length > 0 ? dialed.join("") : <span className="opacity-30">——</span>}
          </span>
          {dialed.length > 0 && (
            <button
              onClick={handleClear}
              className="text-neutral-500 hover:text-red-400 text-xs ml-2 transition-colors"
              aria-label="Clear"
            >
              ✕
            </button>
          )}
        </div>

        {/* Dial */}
        <div className="relative w-52 h-52 rounded-full bg-neutral-700 shadow-inner flex items-center justify-center">
          {/* Center hub */}
          <div className="w-10 h-10 rounded-full bg-neutral-500 shadow z-10" />

          {/* Digit holes */}
          {HOLES.map((digit, i) => {
            const angle = (i / HOLES.length) * 360 - 90;
            const rad = (angle * Math.PI) / 180;
            const r = 80;
            const x = r * Math.cos(rad);
            const y = r * Math.sin(rad);
            const isSpinning = spinning === digit;

            return (
              <button
                key={digit}
                onClick={() => handleDial(digit)}
                style={{ transform: `translate(${x}px, ${y}px)` }}
                className={`absolute w-9 h-9 rounded-full bg-neutral-600 hover:bg-amber-500 active:scale-95
                  text-white font-bold text-sm shadow transition-all duration-150 flex items-center justify-center
                  ${isSpinning ? "bg-amber-400 scale-110 ring-2 ring-amber-300" : ""}
                  disabled:opacity-50`}
                disabled={spinning !== null}
                aria-label={`Dial ${digit}`}
              >
                {digit}
              </button>
            );
          })}
        </div>

        {/* Spin indicator */}
        <p className="mt-4 text-neutral-400 text-xs h-4">
          {spinning !== null ? `Dialing ${spinning}…` : ""}
        </p>
      </div>

      {/* Fact card */}
      <div className="mt-8 bg-white border border-amber-200 rounded-2xl shadow p-5 max-w-sm w-full">
        <p className="text-xs font-semibold text-amber-500 uppercase tracking-wide mb-1">
          Did you know?
        </p>
        <p className="text-neutral-700 text-sm leading-relaxed">{FACTS[factIndex]}</p>
      </div>

      <footer className="mt-10 text-amber-400 text-xs">
        Built with Next.js · Deployed on Vercel
      </footer>
    </main>
  );
}
