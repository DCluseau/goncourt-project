# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Author, JuryMember et Character
"""

from abc import ABC
from dataclasses import dataclass, field



@dataclass
class Person(ABC):
    """Personne liée au prix Goncourt : Person, Author, JuryMember."""
    id_person: int
    firstname: str
    lastname: str

    def __init__(self, id_person: int, firstname: str, lastname: str):
        self.id_person = id_person
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
