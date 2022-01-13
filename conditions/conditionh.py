from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionH(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition):
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        self.__cleaning_from_code()

        for transition in transitions:
            condition: TypesCondition | bool = transition.action()
            if isinstance(condition, TypesCondition):
                self._condition.now = condition
                break

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in [' ', '\n']:
            self._reader.trip_first_character()
