# -*- coding: utf-8 -*-

"""
Classe Author, hérite de Person
"""

from dataclasses import dataclass
from models.person import Person


@dataclass
class Author(Person):
    biography: str
    def __init__(self, id_person: int, firstname: str, lastname: str, biography):
        super().__init__(id_person, firstname, lastname)
        self.biography = biography

    def __str__(self) -> str:
        if self.biography is not None:
            return f"{self.firstname} {self.lastname}\n    - Biographie : {self.biography}\n"
        else:
            return f"{self.firstname} {self.lastname}\n"

