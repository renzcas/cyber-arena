const ws = new WebSocket(`ws://${location.host}/ws/arena`);
const info = document.getElementById("info");

ws.onmessage = (msg) => {
    const state = JSON.parse(msg.data);
    renderScenario(state);
};

function renderScenario(state) {
    info.innerHTML = `
        <p><strong>Tick:</strong> ${state.tick}</p>
        <p><strong>Entities:</strong> ${state.entities.length}</p>
        <p><strong>Nodes:</strong> ${state.nodes.length}</p>
        <p><strong>Events:</strong> ${state.events.length}</p>
    `;
}
