import React from "react";
import { useArenaState } from "./hooks/useArenaState";

export default function ArenaOverviewPanel() {
  const { loading, error, state } = useArenaState();

  if (loading) return <div>Loading Arena…</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="arena-overview">
      <h2>Cyber‑Arena Overview</h2>

      <section>
        <h3>Teams</h3>
        <ul>
          <li>Red: {state.red.status}</li>
          <li>Blue: {state.blue.status}</li>
          <li>Grey: {state.grey.status}</li>
        </ul>
      </section>

      <section>
        <h3>Metrics</h3>
        <p>Attack Intensity: {state.metrics.attack_intensity}</p>
        <p>Defense Load: {state.metrics.defense_load}</p>
      </section>

      <section>
        <h3>Scenario</h3>
        <p>{state.scenario.name}</p>
        <p>Phase: {state.scenario.phase}</p>
      </section>
    </div>
  );
}
