const ws = new WebSocket(`ws://${location.host}/ws/arena`);
const map = document.getElementById("map");

ws.onmessage = (msg) => {
    const state = JSON.parse(msg.data);
    renderNodes(state.nodes || []);
};

function renderNodes(nodes) {
    map.innerHTML = "";

    nodes.forEach(n => {
        const dot = document.createElement("div");
        dot.className = "node";

        dot.style.left = (400 + n.x * 10) + "px";
        dot.style.top = (300 - n.y * 10) + "px";

        map.appendChild(dot);
    });
}
