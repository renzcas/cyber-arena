from .base_env import BaseEnvironment

class CyberEnvironment(BaseEnvironment):
    def __init__(self):
        self.state = {}

    def reset(self):
        self.state = {}
        return self.state

    def step(self, action):
        return {'result': 'ok', 'action': action}

