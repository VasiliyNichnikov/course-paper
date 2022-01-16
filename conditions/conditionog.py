from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionOG(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        self._buffer.clear()
        self._buffer.add(self._reader.selected_symbol)
        self._token.writing_token_to_table(TypesOfTokenTables.LIMITERS)

        if self._token.z != 0:
            self._reader.trip_first_character()
            self._token.writing_to_token_file(1, self._token.z)
            self._condition.now = TypesCondition.H
        else:
            self._condition.now = TypesCondition.ER
