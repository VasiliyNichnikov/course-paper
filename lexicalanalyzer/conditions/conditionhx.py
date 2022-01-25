from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from myutils import converting_numbers_writing_to_tokens
from tokens.workingwithtoken import WorkingWithToken


class ConditionHX(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_letter(self._reader.selected_symbol) \
                or checking_symbol.is_value_number(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            converting_numbers_writing_to_tokens(self._buffer, self._token, 16)
            self._condition.now = TypesCondition.H
