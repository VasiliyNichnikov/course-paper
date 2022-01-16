from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent
from conditions.typescondition import TypesCondition


class ConditionC2(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        self.__clearing_from_code()
        if self._reader.selected_symbol == '}':
            self._condition = TypesCondition.ER
        else:
            self._reader.trip_first_character()
            self._condition = TypesCondition.C3

    def __clearing_from_code(self) -> None:
        while self._reader.selected_symbol != '*' and self._reader.selected_symbol != '}':
            self._reader.trip_first_character()
