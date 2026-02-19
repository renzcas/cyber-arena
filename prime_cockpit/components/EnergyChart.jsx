import React from "react";

export function EnergyChart({ series }) {
  const colorForRole = role =>
    role === "RED" ? "#ff4d4f" : role === "BLUE" ? "#40a9ff" : role === "PURPLE" ? "#9254de" : "#999";

  return (
    <svg width={400} height={200} style={{ background: "#111" }}>
      {series.map(s => {
        const color = colorForRole(s.role);
        const pts = s.points;
        if (!pts.length) return null;

        const tMin = pts[0][0];
        const tMax = pts[pts.length - 1][0];
        const Ls = pts.map(p => p[1]);
        const Hs = pts.map(p => p[2]);
        const vMin = Math.min(...Ls, ...Hs);
        const vMax = Math.max(...Ls, ...Hs);

        const xScale = t => ((t - tMin) / Math.max(tMax - tMin || 1, 1e-6)) * 380 + 10;
        const yScale = v => 190 - ((v - vMin) / Math.max(vMax - vMin || 1, 1e-6)) * 180;

        const pathL = pts.map((p, i) => `${i === 0 ? "M" : "L"} ${xScale(p[0])} ${yScale(p[1])}`).join(" ");
        const pathH = pts.map((p, i) => `${i === 0 ? "M" : "L"} ${xScale(p[0])} ${yScale(p[2])}`).join(" ");

        return (
          <g key={s.agent_id}>
            <path d={pathH} stroke={color} strokeWidth={1} fill="none" opacity={0.4} />
            <path d={pathL} stroke={color} strokeWidth={2} fill="none" />
          </g>
        );
      })}
    </svg>
  );
}
