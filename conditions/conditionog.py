from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
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
        super(ConditionOG, self).action(transitions)
