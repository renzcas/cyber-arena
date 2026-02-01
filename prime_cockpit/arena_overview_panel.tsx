import React from "react";
import { useArenaState } from "../hooks/useArenaState";

export const ArenaOverviewPanel: React.FC = () => {
  const { loading, error, state } = useArenaState();

  if (loading) return <div>Loading arena state…</div>;
  if (error) return <div>Error loading arena: {error}</div>;

  return (
    <div className="arena-overview">
      <h2>Arena Overview</h2>
      <div className="arena-grid">
        <section>
          <h3>Actors</h3>
          <ul>
            <li>Red: {state.red_team.status}</li>
            <li>Blue: {state.blue_team.status}</li>
            <li>Grey: {state.grey_team.status}</li>
          </ul>
        </section>
        <section>
          <h3>Pressure & Load</h3>
          <p>Attack intensity: {state.metrics.attack_intensity}</p>
          <p>Defense load: {state.metrics.defense_load}</p>
        </section>
        <section>
          <h3>Current Scenario</h3>
          <p>{state.scenario.name}</p>
          <p>{state.scenario.phase}</p>
        </section>
      </div>
    </div>
  );
};
