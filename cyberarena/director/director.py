class Director:
    def __init__(self, environment):
        self.environment = environment

    def run_step(self, action):
        return self.environment.step(action)

