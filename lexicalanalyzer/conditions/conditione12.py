from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from myutils import reading_next_character, converting_string_to_numbers_writing_to_tokens
from tokens.workingwithtoken import WorkingWithToken


class ConditionE12(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()

        self.__cleaning_from_code(checking_symbol)
        if checking_symbol.check_hex(self._reader.selected_symbol):
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            converting_string_to_numbers_writing_to_tokens(self._buffer, self._token)
            self._condition.now = TypesCondition.H

    def __cleaning_from_code(self, checking_symbol: CheckingSymbol) -> None:
        while checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
