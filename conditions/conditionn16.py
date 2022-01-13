from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from myutils import reading_next_character
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionN16(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        self.__cleaning_from_code()
        super(ConditionN16, self).action(transitions)

    def __cleaning_from_code(self) -> None:
        reading_next_character(self._buffer, self._reader)
