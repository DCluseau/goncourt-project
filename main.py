#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du Prix Goncourt
"""
from business.goncourt import Goncourt
from models.selection import Selection


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
        Prix Goncourt
--------------------------""")

    goncourt: Goncourt = Goncourt()

    goncourt.read_selections()
    print(goncourt)

    goncourt.selections[0].votes['9782073080028'] = 1
    goncourt.update_vote(goncourt.selections[0], '9782073080028')

    print(goncourt.selections[0])
if __name__ == '__main__':
    main()
