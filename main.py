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
if __name__ == '__main__':
    main()
