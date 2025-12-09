# -*- coding: utf-8 -*-

"""
Classe JuryMember, hérite de Person
"""

from dataclasses import dataclass, field

from models.person import Person


@dataclass
class JuryMember(Person):
    president: bool

    def __init__(self, id_person: int, firstname: str, lastname: str, president: bool):
        super().__init__(id_person, firstname, lastname)
        self.president = president

