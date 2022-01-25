from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from myutils import reading_next_character
from tokens.workingwithtoken import WorkingWithToken


class ConditionN16(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__cleaning_from_code()
        if self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        else:
            self._condition.now = TypesCondition.ER

    def __cleaning_from_code(self) -> None:
        checking_symbol = CheckingSymbol()
        while checking_symbol.check_hex(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
