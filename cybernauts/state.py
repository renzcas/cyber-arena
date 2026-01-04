class CybernautState:
    """
    Lightweight state container for Cybernaut memory and status.
    Prime Cockpit expects:
        - add_memory(entry)
        - get_recent_memory(n)
    """

    def __init__(self):
        # rolling memory buffer
        self.memory = []
        self.max_memory = 50

    def add_memory(self, entry):
        """Append a memory entry and keep buffer bounded."""
        self.memory.append(entry)
        if len(self.memory) > self.max_memory:
            self.memory.pop(0)

    def get_recent_memory(self, n=5):
        """Return the last n memory entries."""
        return self.memory[-n:]
