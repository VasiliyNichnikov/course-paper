from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from myutils import converting_numbers_writing_to_tokens
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionO(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_letter(self._reader.selected_symbol) or checking_symbol.is_value_number(
                self._reader.selected_symbol):
            self._condition = TypesCondition.ER
        else:
            converting_numbers_writing_to_tokens(self._buffer, self._token, 8)
            self._condition.now = TypesCondition.H
