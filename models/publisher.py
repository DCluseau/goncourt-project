# -*- coding: utf-8 -*-

"""
Classe Publisher
"""

from dataclasses import dataclass

@dataclass
class Publisher:
    id_publisher: int
    name: str

    def __init__(self, id_publisher: int, name: str):
        self.id_publisher = id_publisher
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

