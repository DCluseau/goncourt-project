# -*- coding: utf-8 -*-

"""
Classe Book
"""

from dataclasses import dataclass
from datetime import date
from time import strftime

from models import character
from models.author import Author
from models.publisher import Publisher

@dataclass
class Book:
    isbn: str
    title: str
    summary: str
    publication_date: date
    number_of_page: int
    publisher_price: float
    prize: bool
    author: Author
    publisher: Publisher
    characters: list[character.Character]

    def __init__(self, isbn: str, title: str, summary: str, publication_date: date, number_of_page: int, publisher_price: float, prize: bool, author_: Author, publisher_: Publisher, characters: list[character.Character]):
        self.isbn = isbn
        self.title = title
        self.summary = summary
        self.publication_date = publication_date
        self.number_of_page = number_of_page
        self.publisher_price = publisher_price
        self.prize = prize
        self.author = author_
        self.publisher = publisher_
        self.characters = characters

    def __str__(self) -> str:
        if self.summary is not None:
            summary = f"Résumé : {self.summary}"
        else:
            summary = "Résumé non renseigné"
        characters = self.display_characters()
        if characters != "":
            characters = f"Personnages :\n{characters}"
        else:
            characters = "Personnages non renseignés"
        return f"\nISBN : {self.isbn}\n - Titre: {self.title}\n - Auteur : {self.author.firstname} {self.author.lastname}\n - Prix : {self.publisher_price}\n - Editeur : {self.publisher.name}\n - Nombre de pages : {self.number_of_page}\n - Date de parution : {self.publication_date.strftime("%d/%m/%Y")}\n - {summary}\n - {characters}\n"

    def display_characters(self):
        characters_list: str = ""
        for charac in self.characters:
            characters_list += f"    - {charac.firstname} {charac.lastname}"
        return characters_list

