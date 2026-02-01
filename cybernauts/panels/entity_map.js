const ws = new WebSocket(`ws://${location.host}/ws/arena`);
const map = document.getElementById("map");

ws.onmessage = (msg) => {
    const state = JSON.parse(msg.data);
    renderEntities(state.entities);
};

function renderEntities(entities) {
    map.innerHTML = "";

    entities.forEach(e => {
        const dot = document.createElement("div");
        dot.className = "entity";

        dot.style.left = (400 + e.x * 10) + "px";
        dot.style.top = (300 - e.y * 10) + "px";

        map.appendChild(dot);
    });
}
