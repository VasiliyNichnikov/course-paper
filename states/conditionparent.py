from abc import abstractmethod, ABC
from typing import List

from characterreader import CharacterReader
# from buffer import Buffer
from states.condition import Condition
# from checkingsymbol import CheckingSymbol
# from tokens.workingwithtoken import WorkingWithToken
from transitions.transitionparent import TransitionParent


# checking_symbol: CheckingSymbol, buffer: Buffer,
#                  token: WorkingWithToken

class ConditionParent(ABC):
    def __init__(self, reader: CharacterReader, condition: Condition) -> None:
        self._reader = reader
        self._condition = Condition
        # self._checking_symbol = checking_symbol
        # self._buffer = buffer
        # self._token = token

    @abstractmethod
    def action(self, transitions: List[TransitionParent]) -> None:
        pass
