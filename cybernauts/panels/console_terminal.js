function sendCommand() {
    const channel = document.getElementById("channel").value;
    const commandText = document.getElementById("command").value;

    let command;
    try {
        command = JSON.parse(commandText);
    } catch {
        alert("Invalid JSON");
        return;
    }

    fetch("/api/console/command", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ channel, command })
    });
}
