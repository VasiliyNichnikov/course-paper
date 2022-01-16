from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from myutils import reading_next_character
from tokens.workingwithtoken import WorkingWithToken


class ConditionN8(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        self.__cleaning_from_code()
        if self._reader.selected_symbol in ['8', '9']:
            self._condition.now = TypesCondition.N10
        elif self._reader.selected_symbol in ['A', 'a', 'B', 'b', 'C', 'c', 'F', 'f']:
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['E', 'e']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.E11
        elif self._reader.selected_symbol in ['D', 'd']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.D
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif self._reader.selected_symbol == '.':
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol in ['O', 'o']:
            self._buffer.add(self._reader.selected_symbol)
            self._condition.now = TypesCondition.O
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._condition.now = TypesCondition.N10

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in ['2', '3', '4', '5', '6', '7']:
            reading_next_character(self._buffer, self._reader)
