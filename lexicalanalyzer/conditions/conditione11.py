from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from myutils import reading_next_character
from tokens.workingwithtoken import WorkingWithToken


class ConditionE11(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_number(self._reader.selected_symbol) \
                or checking_symbol.is_value_letter(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.E12
        elif self._reader.selected_symbol in ['+', '-']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.ZN
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.check_hex(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N16
        else:
            self._condition.now = TypesCondition.ER
