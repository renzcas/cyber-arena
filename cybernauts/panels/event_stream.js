const ws = new WebSocket(`ws://${location.host}/ws/arena`);
const log = document.getElementById("log");

ws.onmessage = (msg) => {
    const state = JSON.parse(msg.data);
    state.events.slice(-5).forEach(e => appendEvent(e));
};

function appendEvent(e) {
    const div = document.createElement("div");
    div.textContent = `[${new Date(e.timestamp).toLocaleTimeString()}] ${e.type}`;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
}
