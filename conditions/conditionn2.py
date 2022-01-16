from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from myutils import reading_next_character
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionN2(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__cleaning_from_code()
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['2', '3', '4', '5', '6', '7']:
            self._condition.now = TypesCondition.N8
        elif self._reader.selected_symbol in ['8', '9']:
            self._condition.now = TypesCondition.N10
        elif self._reader.selected_symbol in ['A', 'a', 'C', 'c', 'F', 'f']:
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['E', 'e']:
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.E11
        elif self._reader.selected_symbol in ['D', 'd']:
            self._buffer.add(self._reader.selected_symbol)
            self._condition.now = TypesCondition.D
        elif self._reader.selected_symbol in ['O', 'o']:
            self._condition.now = TypesCondition.O
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif self._reader.selected_symbol == '.':
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol in ['B', 'b']:
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.B
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._condition.now = TypesCondition.N10

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in ['0', '1']:
            reading_next_character(self._buffer, self._reader)
