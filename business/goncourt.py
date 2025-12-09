# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field
from typing import Optional

from daos.dao import Dao
from daos.selection_dao import SelectionDao
from models.selection import Selection

## PRENDRE EN COMPTE QU'ON N'EST QUE LE 03/09 et que le président sélectionne les romans pour les deux autres tours

@dataclass
class Goncourt:
    """Couche métier de l'application de gestion du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles
    """

    selections: list[Selection]

    def add_selection(self, selection: Selection) -> None:
        """Ajout du cours course à la liste des cours."""
        self.selections.append(selection)


    def read_selections(self):
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id FROM selection"
            cursor.execute(sql,)
            record = cursor.fetchall()
        if record is not None:
            self.add_selection(SelectionDao.read(record['id']))
        else:
            self.selections = []