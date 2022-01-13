from typing import List

from characterreader import CharacterReader
from states.condition import Condition
from states.conditionparent import ConditionParent
from states.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class ConditionH(ConditionParent):

    def __init__(self, reader: CharacterReader, condition: Condition):
        super().__init__(reader, condition)

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
