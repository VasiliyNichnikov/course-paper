from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionM1(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '>':
            self._reader.trip_first_character()
            self._token.writing_to_token_file(1, 17)
        elif self._reader.selected_symbol == '=':
            self._reader.trip_first_character()
            self._token.writing_to_token_file(1, 20)
        else:
            self._token.writing_to_token_file(1, 19)
        self._condition.now = TypesCondition.H
