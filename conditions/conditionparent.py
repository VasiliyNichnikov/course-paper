from abc import abstractmethod, ABC
from typing import List

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.typescondition import TypesCondition
from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


class ConditionParent(ABC):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        self._reader = reader
        self._condition = condition
        self._buffer = buffer
        self._token = token

    def action(self, transitions: List[TransitionParent]) -> None:
        for transition in transitions:
            condition: TypesCondition | bool = transition.action()
            if isinstance(condition, TypesCondition):
                self._condition.now = condition
                break
