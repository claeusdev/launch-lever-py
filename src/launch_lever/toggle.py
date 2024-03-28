from dataclasses import dataclass


@dataclass
class Toggle(object):
    name: str
    description: str
    status: str
