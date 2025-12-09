# -*- coding: utf-8 -*-

"""
Classe Dao[Person]
"""
from models.author import Author
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorDao(Dao[Author]):

    def create(self, author: Author) -> int:
        pass

    def update(self, author: Author) -> bool:
        pass

    def delete(self, author: Author) -> bool:
        pass

    def read(self, id_author: int) -> Optional[Author]:
        """Renvoie l'auteur' correspondant à l'entité dont l'id est id_author
           (ou None s'il n'a pu être trouvé)"""
        author: Optional[Author]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT person.firstname, person.lastname, author.id, author.biography FROM person INNER JOIN author ON person.id = author.id_person WHERE author.id = %s"
            cursor.execute(sql, (id_author,))
            record = cursor.fetchone()
        if record is not None:
            author = Author(record['id'], record['firstname'], record['lastname'], record['biography'])
        else:
            author = None
        return author
