from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionD(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) ->None:
        super().__init__(reader, buffer, token, condition)
        
    def action(self, transitions: List[TransitionParent]) -> None:
        super(ConditionD, self).action(transitions)