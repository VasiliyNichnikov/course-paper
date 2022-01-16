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


class ConditionE21(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition):
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['+', '-']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.ZN
        elif checking_symbol.is_value_number(self._reader.selected_symbol):
            self._condition.now = TypesCondition.E22
        else:
            self._condition.now = TypesCondition.ER
