from .registry import get

class OrganFactory:
    @staticmethod
    def create(name, **kwargs):
        cls = get(name)
        if not cls:
            raise ValueError(f'Unknown organ: {name}')
        return cls(**kwargs)

