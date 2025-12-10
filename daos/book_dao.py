# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""
from daos.author_dao import AuthorDao
from daos.character_dao import CharacterDao
from daos.publisher_dao import PublisherDao
from models.author import Author
from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.character import Character
from models.publisher import Publisher


@dataclass
class BookDao(Dao[Book]):

    def create(self, book: Book) -> int:
        pass

    def update(self, book: Book) -> bool:
        pass

    def delete(self, book: Book) -> bool:
        pass

    def read(self, isbn: str) -> Optional[Book]:
        """Renvoie l'éditeur correspondant à l'entité dont l'id est isbn
           (ou None s'il n'a pu être trouvé)"""
        book: Optional[Book]
        characters_list: list[Character] = []
        author: Optional[Author]|None
        publisher: Optional[Publisher]|None

        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_person FROM is_character WHERE is_character.isbn = %s"
            cursor.execute(sql, (isbn,))
            record = cursor.fetchall()
            if record is not None:
                for row in record:
                    characters_list.append(CharacterDao.read(CharacterDao(), row['id_person']))
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_author FROM book WHERE isbn = %s"
            cursor.execute(sql, (isbn,))
            record = cursor.fetchone()
            if record is not None:
                author = AuthorDao.read(AuthorDao(), record['id_author'])
            else:
                author = None
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_publisher FROM book WHERE isbn = %s"
            cursor.execute(sql, (isbn,))
            record = cursor.fetchone()
            if record is not None:
                publisher = PublisherDao.read(PublisherDao(), record['id_publisher'])
            else:
                publisher = None
        with Dao.connection.cursor() as cursor:
            sql = "SELECT title, summary, publication_date, number_of_pages, publisher_price, id_author, prize, id_publisher FROM book LEFT OUTER JOIN is_character ON book.isbn = is_character.isbn WHERE book.isbn = %s"
            cursor.execute(sql, (isbn,))
            record = cursor.fetchone()
            if record is not None:
                book = Book(isbn, record['title'], record['summary'], record['publication_date'], record['number_of_pages'], record['publisher_price'], record['prize'], author, publisher, characters_list)
            else:
                book = None
        return book