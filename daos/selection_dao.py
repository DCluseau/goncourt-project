# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""
from daos.book_dao import BookDao
from daos.jury_member_dao import JuryMemberDao
from models.book import Book
from models.jury_member import JuryMember
from models.selection import Selection
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class SelectionDao(Dao[Selection]):
    def update(self, selection: Selection) -> bool:
        pass

    def delete(self, selection: Selection) -> bool:
        pass

    def create(self, selection: Selection) -> int:
        pass

    def read(self, id_selection: int) -> Optional[Selection]:
        """Renvoie la sélection correspondant à l'entité dont l'id est id_selection
           (ou None s'il n'a pu être trouvé)"""
        selection: Optional[Selection]
        jury_member: JuryMemberDao
        jury_members: list[JuryMember] = []
        book: Optional[Book]
        books: dict[Book, int] = {}
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_person FROM is_jury_member WHERE id_selection = %s"
            cursor.execute(sql, id_selection,)
            record = cursor.fetchall()
            if record is not None:
                for row in record:
                    jury_members.append(JuryMemberDao.read(JuryMemberDao(),[row['id_person'], id_selection]))
        with Dao.connection.cursor() as cursor:
            sql = "SELECT isbn, number_of_votes FROM is_selected WHERE id_selection = %s"
            cursor.execute(sql, id_selection,)
            record = cursor.fetchall()
            if record is not None:
                for row in record:
                    book = BookDao.read(BookDao(),row['isbn'])
                    books[book] = row['number_of_votes']
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id, round, year_selection FROM selection WHERE selection.id = %s"
            cursor.execute(sql, (id_selection,))
            record = cursor.fetchone()
            if record is not None:
                selection = Selection(record['id'], record['round'], record['year_selection'], jury_members, books)
            else:
                selection = None
        return selection
