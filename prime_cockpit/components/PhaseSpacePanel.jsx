import React, { useEffect, useState } from "react";

export function PhaseSpacePanel() {
  const [series, setSeries] = useState([]);

  useEffect(() => {
    async function fetchPhase() {
      const res = await fetch("/telemetry/phase_space");
      const data = await res.json();
      setSeries(data.series || []);
    }
    fetchPhase();
    const id = setInterval(fetchPhase, 3000);
    return () => clearInterval(id);
  }, []);

  if (!series.length) return <div>Loading phase space…</div>;

  const colorForRole = role =>
    role === "RED" ? "#ff4d4f" : role === "BLUE" ? "#40a9ff" : role === "PURPLE" ? "#9254de" : "#999";

  return (
    <div className="phase-space-panel">
      <h3>Agent Phase Space</h3>
      <svg width={400} height={200} style={{ background: "#111" }}>
        {series.map(s => {
          const pts = s.points;
          if (!pts.length) return null;

          const xVals = pts.map(p => p.x);
          const yVals = pts.map(p => p.y);
          const xMin = Math.min(...xVals);
          const xMax = Math.max(...xVals);
          const yMin = Math.min(...yVals);
          const yMax = Math.max(...yVals);

          const xScale = x => ((x - xMin) / Math.max(xMax - xMin || 1, 1e-6)) * 380 + 10;
          const yScale = y => 190 - ((y - yMin) / Math.max(yMax - yMin || 1, 1e-6)) * 180;

          const path = pts
            .map((p, i) => `${i === 0 ? "M" : "L"} ${xScale(p.x)} ${yScale(p.y)}`)
            .join(" ");

          return (
            <g key={`${s.agent_id}-${s.coord}`}>
              <path d={path} stroke={colorForRole(s.role)} strokeWidth={1.5} fill="none" opacity={0.8} />
            </g>
          );
        })}
      </svg>
    </div>
  );
}
