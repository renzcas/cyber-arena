ORGANS = {}

def register(name, cls):
    ORGANS[name] = cls

def get(name):
    return ORGANS.get(name)

