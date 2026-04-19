_REGISTRY = {}

# 辞書に登録
def register(cls):
    _REGISTRY[cls.name] = cls
    return cls

def get_algorithm(name):
    if name not in _REGISTRY:
        raise ValueError(f"Unknown algorithm: '{name}'")
    return _REGISTRY[name]

def available_algorithms() -> list[str]:
    return sorted(_REGISTRY.keys())

from mazegen.algorithms import prim