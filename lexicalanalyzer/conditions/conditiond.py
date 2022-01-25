from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken


class ConditionD(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.check_hex(self._reader.selected_symbol):
            self._condition.now = TypesCondition.N16
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._token.writing_token_to_table(TypesOfTokenTables.NUMBERS)
            self._token.writing_token_to_file(TypesOfTokenTables.NUMBERS, self._token.z)
            self._condition.now = TypesCondition.H
