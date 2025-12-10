# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""

from models.character import Character
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class CharacterDao(Dao[Character]):

    def create(self, character: Character) -> int:
        pass

    def update(self, character: Character) -> bool:
        pass

    def delete(self, character: Character) -> bool:
        pass

    def read(self, id_person: int) -> Optional[Character]:
        """Renvoie l'auteur' correspondant à l'entité dont l'id est id_author
           (ou None s'il n'a pu être trouvé)"""
        character: Optional[Character]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT person.id, person.firstname, person.lastname, character.isbn FROM person INNER JOIN is_character ON person.id = is_character.id_person WHERE person.id = %s"
            cursor.execute(sql, (id_person,))
            record = cursor.fetchone()
        if record is not None:
            character = Character(record['id'], record['firstname'], record['lastname'], record['isbn'])
        else:
            character = None
        return character

    @staticmethod
    def read_all(isbn: int) -> Optional[list[Character]]:
        """Renvoie l'auteur' correspondant à l'entité dont l'id est id_author
                   (ou None s'il n'a pu être trouvé)"""
        character: Optional[Character]
        characters_list: list[Character] = []
        with Dao.connection.cursor() as cursor:
            sql = "SELECT person.id, person.firstname, person.lastname FROM person INNER JOIN character ON person.id = is_character.id_person WHERE is_character.isbn = %s"
            cursor.execute(sql, (isbn,))
            record = cursor.fetchall()
        if record is not None:
            for row in record:
                character = Character(row['id'], row['firstname'], row['lastname'], row['isbn'])
                characters_list.append(character)
        else:
            characters_list = []
        return characters_list