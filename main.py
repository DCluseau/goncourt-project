#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du Prix Goncourt
"""
from business.goncourt import Goncourt
from daos.selection_dao import SelectionDao
from models.selection import Selection


def choose_year():
    year_choice = int(input("Veuillez entrer l'année sur laquelle vous voulez travailler (format AAAA) : "))
    return year_choice

def display_main_menu(is_jury_president: bool) -> None:
    """

    :rtype: None
    """
    print("Veuillez sélectionner une action\n")

    print("1 - Sélectionner la sélection sur laquelle travailler")
    print("2 - Afficher les livres sélectionnés")
    print("3 - Modifier l'année sur laquelle travailler")
    if is_jury_president:
        print("\nRéservé au président du jury : \n")
        print("4 - Ajouter un livre à une sélection")
        print("5 - Ajouter les votes à un livre")
        print("6 - Indiquer quel livre a réçu le prix")
    print("0 - Quitter le programme")


def select_selection(year: int):
    print("==================================")
    print("      CHOIX DE LA SÉLECTION")
    print("==================================\n")
    nb_round = int(input(f"Pour quel tour voulez-vous afficher la sélection ? (année {year})\n"))
    return 1

def add_book_to_select():
    print("==================================")
    print(" AJOUTER UN LIVRE A UNE SELECTION")
    print("==================================\n")

def set_votes(year: int, selected_round: int, goncourt: Goncourt):
    id_selection:int = 0
    print("==================================")
    print("       SAISIR LES VOTES")
    print("==================================\n")

    print(f"\nConcours de l'année {year} - Tour numéro {selected_round}\n")

    for x in range(len(goncourt.selections)):
        if goncourt.selections[x].year == year and goncourt.selections[x].round_nb == selected_round:
            print(goncourt.selections[x].display_books())

            selected_book: str = input("Veuillez saisir l'ISBN du livre à modifier : ")
            nb_votes: int = int(input("Veuillez entrer le nombre de votes total pour le livre sélectionné : "))

            goncourt.selections[x].votes[selected_book] = nb_votes
            goncourt.update_vote(goncourt.selections[x], selected_book)
            break

def choose_winner(year: int):
    print("==================================")
    print("         DÉCERNER LE PRIX")
    print("==================================\n")

def display_selected_books(year: int, selected_round: int):
    print("==================================")
    print(" AFFICHER LES LIVRES SÉLECTIONNÉS")
    print("==================================\n")

def main() -> None:
    year_choice:int = 0
    is_jury_president: bool = False
    menu_choice:int = -1
    nb_round: int = 0

    goncourt: Goncourt = Goncourt()

    goncourt.read_selections()

    """Programme principal."""
    print("""\
--------------------------
        Prix Goncourt
--------------------------

Bienvenue !\n""")

    print("==================================")
    print("          MENU PRINCIPAL")
    print("==================================\n")

    ## CHOIX DE L'ANNÉE ##
    year_choice = choose_year()
    nb_round = select_selection(year_choice)

    ## SAISIR LE PRESIDENT DU JURY ##
    if input("Êtes-vous le président du jury ? Y/N : ") == "Y":
        is_jury_president = True

    display_main_menu(is_jury_president)

    menu_choice = int(input("Choix : "))
    while menu_choice != 0:
        match menu_choice:
            case 0:
                ## QUITTER LE PROGRAMME ##
                pass
            case 1:
                ## MENU 1 : CHOIX DE LA SÉLECTION ##
                nb_round = select_selection(year_choice)
            case 2:
                ## MENU 2 : AFFICHER LES LIVRES SÉLECTIONNÉS #
                display_selected_books(year_choice, nb_round)
            case 3:
                ## MENU 3 : MODIFIER L'ANNÉE #
                year_choice = choose_year()
            ## CAS RESERVES AU PRESIDENT DU JURY
            case 4:
                ## MENU 4 : AJOUTER UN LIVRE A UNE SELECTION ##
                # Note : les livres sont déjà dans la BDD #
                add_book_to_select()
            case 5:
                ## MENU 5 : SAISIR LES VOTES ##
                set_votes(year_choice, nb_round, goncourt)
            case 6:
                ## MENU 6 : INDIQUER LE LIVRE QUI A RECU LE PRIX ##
                choose_winner(year_choice)
            case _:
                display_main_menu(is_jury_president)
        display_main_menu(is_jury_president)
        menu_choice = int(input("Choix : "))

    print(goncourt)

if __name__ == '__main__':
    main()
