from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.conditionparent import ConditionParent
from conditions.condition import Condition
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionZN(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self, transitions: List[TransitionParent]) -> None:
        super(ConditionZN, self).action(transitions)
