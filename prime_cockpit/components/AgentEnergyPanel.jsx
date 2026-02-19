import React, { useEffect, useState } from "react";
import { EnergyChart } from "./EnergyChart";

export function AgentEnergyPanel() {
  const [series, setSeries] = useState([]);

  useEffect(() => {
    async function fetchEnergy() {
      const res = await fetch("/telemetry/energy");
      const data = await res.json();
      setSeries(data.series || []);
    }
    fetchEnergy();
    const id = setInterval(fetchEnergy, 2000);
    return () => clearInterval(id);
  }, []);

  if (!series.length) return <div>Loading energy…</div>;

  const latest = series.map(s => {
    const last = s.points[s.points.length - 1];
    return { agent_id: s.agent_id, role: s.role, L: last ? last[1] : 0, H: last ? last[2] : 0 };
  });

  return (
    <div className="agent-energy-panel">
      <div className="agent-energy-header">
        {latest.map(a => (
          <div key={a.agent_id} className={`energy-card role-${a.role.toLowerCase()}`}>
            <div>{a.role} ({a.agent_id})</div>
            <div>L: {a.L.toFixed(2)}</div>
            <div>H: {a.H.toFixed(2)}</div>
          </div>
        ))}
      </div>
      <EnergyChart series={series} />
    </div>
  );
}
