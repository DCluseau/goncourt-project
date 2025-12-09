# -*- coding: utf-8 -*-

"""
Classe Character, hérite de Person
"""

from dataclasses import dataclass, field

from models.person import Person


@dataclass
class Character(Person):

    def __init__(self, id_person: int, firstname: str, lastname: str):
        super().__init__(id_person, firstname, lastname)

