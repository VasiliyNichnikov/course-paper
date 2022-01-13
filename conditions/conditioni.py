from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionI(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        self.__cleaning_from_code()
        self.__search_token_in_service_table()

        for transition in transitions:
            condition: TypesCondition | bool = transition.action()
            if isinstance(condition, TypesCondition):
                self._condition.now = condition
                break

    def __cleaning_from_code(self) -> None:
        checking_symbol = CheckingSymbol()
        while checking_symbol.is_value_letter(self._reader.selected_symbol) or \
                checking_symbol.is_value_number(self._reader.selected_symbol):
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()

    def __search_token_in_service_table(self) -> None:
        self._token.find_token_in_selected_table(TypesOfTokenTables.SERVICE)
