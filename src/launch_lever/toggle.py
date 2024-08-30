from dataclasses import dataclass


@dataclass
class Toggle(object):
    name: str
    description: str
    is_enabled: bool
    conditions: list
    rollout_percentage: int
