# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field

from daos.book_dao import BookDao
from daos.dao import Dao
from daos.selection_dao import SelectionDao
from models.book import Book
from models.selection import Selection

## PRENDRE EN COMPTE QU'ON N'EST QUE LE 03/09 et que le président sélectionne les romans pour les deux autres tours

@dataclass
class Goncourt:
    """Couche métier de l'application de gestion du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles
    """

    selections: list[Selection] = field(default_factory=list)

    def __init__ (self):
        self.selections = []

    def add_selection(self, selection: Selection) -> None:
        self.selections.append(selection)

    def read_selections(self):
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id FROM selection"
            cursor.execute(sql,)
            record = cursor.fetchall()
        if record is not None:
            for row in record:
                self.add_selection(SelectionDao.read(SelectionDao(), row['id']))
        else:
            self.selections = []

    def __str__(self):
        selection_str = ""
        for selection in self.selections:
            selection_str += f"{selection}"
        return selection_str

    @staticmethod
    def update_vote(selection: Selection, isbn: str) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE is_selected SET number_of_votes = %s WHERE isbn = %s and id_selection = %s"
            cursor.execute(sql, (selection.votes[isbn], isbn, selection.id_selection),)
            Dao.connection.commit()
            if cursor.rowcount is not None and cursor.rowcount > 0:
                return True
            else:
                return False

    @staticmethod
    def add_book(isbn: str, id_selection: int, nb_of_votes: int) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO is_selected (isbn, id_selection, number_of_votes) VALUES (%s, %s, %s)"
            cursor.execute(sql, (isbn, id_selection, nb_of_votes),)
            Dao.connection.commit()
            if cursor.rowcount is not None and cursor.rowcount > 0:
                return True
            else:
                return False

    @staticmethod
    def print_all_books():
        list_of_books: list[Book] = BookDao().read_all_books()
        list_of_books_str: str = ""
        for book in list_of_books:
            list_of_books_str += f" - {book.isbn} - {book.title} - {book.author.firstname} {book.author.lastname}\n"
        return list_of_books_str
