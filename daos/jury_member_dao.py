# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""

from models.jury_member import JuryMember
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class JuryMemberDao(Dao[JuryMember]):

    def create(self, jury_member: JuryMember) -> int:
        pass

    def update(self, jury_member: JuryMember) -> bool:
        pass

    def delete(self, jury_member: JuryMember) -> bool:
        pass

    def read(self, jury_person: list[int]) -> Optional[JuryMember]:
        """Renvoie le membre du jury correspondant à l'entité dont l'id est jury_person[0] et dont id_selection est jury_person[1]
           (ou None s'il n'a pu être trouvé)"""
        jury_member: Optional[JuryMember]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT person.firstname, person.lastname FROM person INNER JOIN jury_member ON person.id = is_jury_member.id_person WHERE person.id = %s AND is_jury_member.id_selection = %s"
            cursor.execute(sql, (jury_person[0], jury_person[1]))
            record = cursor.fetchone()
        if record is not None:
            jury_member = JuryMember(record['id'], record['firstname'], record['lastname'], record['presiding'])
        else:
            jury_member = None
        return jury_member
