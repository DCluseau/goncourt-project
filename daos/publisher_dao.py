# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""
from models.publisher import Publisher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class PublisherDao(Dao[Publisher]):

    def create(self, publisher: Publisher) -> int:
        pass

    def update(self, publisher: Publisher) -> bool:
        pass

    def delete(self, publisher: Publisher) -> bool:
        pass

    def read(self, id_publisher: int) -> Optional[Publisher]:
        """Renvoie l'éditeur correspondant à l'entité dont l'id est id_publisher
           (ou None s'il n'a pu être trouvé)"""
        publisher: Optional[Publisher]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT id, name FROM publisher WHERE publisher.id = %s"
            cursor.execute(sql, (id_publisher,))
            record = cursor.fetchone()
        if record is not None:
            publisher = Publisher(record['id'], record['name'])
        else:
            publisher = None
        return publisher
