# -*- coding: utf-8 -*-

"""
Classe Publisher
"""

from abc import ABC
from dataclasses import dataclass, field

@dataclass
class Publisher(ABC):
    id_publisher: int
    name: str

    def __init__(self, id_publisher: str, name: str):
        self.id_publisher = id_publisher
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

