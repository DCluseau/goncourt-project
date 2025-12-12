# -*- coding: utf-8 -*-

"""
Classe Selection
"""

from dataclasses import dataclass
from datetime import datetime

from models.jury_member import JuryMember
from models.book import Book


@dataclass
class Selection:
    id_selection: int
    round_nb: int
    year: datetime
    jury_members: list[JuryMember]
    books: list[Book]
    votes: dict[str, int]

    def __init__(self, id_selection: int, round_nb: int, year: datetime, jury_members: list[JuryMember], books: list[
        Book], votes: dict[str, int]):
        self.id_selection = id_selection
        self.round_nb = round_nb
        self.year = year
        self.jury_members = jury_members
        self.books = books
        self.votes = votes

    def __str__(self) -> str:
        return f"\nAnnée : {self.year}\nMembres du jury : {self.display_jury_members()}\nTour numéro {self.round_nb}\nSélection de livres :\n{self.display_books()}"

    def set_vote(self, book: Book, nb_of_votes: int):
        self.votes[book.isbn] = nb_of_votes

    def display_books(self):
        book_str: str = ""
        gagnant_str: str = ""
        for book in self.books:
            if book.prize:
                gagnant_str = f"Gagnant : \n{book}"
            else:
                book_str += f"{book}"
                book_str += f"Nombre de votes : {self.votes[book.isbn]}"
                book_str += "\n------------------------------------------------------"
        return gagnant_str + book_str

    def display_jury_members(self):
        jury_members_str: str = ""
        jury_member_president: str = ""
        for jury_member in self.jury_members:
            if jury_member.president:
                jury_member_president = f"\n - {str(jury_member)} (président du jury)\n"
            else:
                jury_members_str += f"\n - {str(jury_member)}"
        return jury_member_president + jury_members_str