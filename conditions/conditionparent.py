from abc import abstractmethod, ABC

from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from tokens.workingwithtoken import WorkingWithToken


class ConditionParent(ABC):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        self._reader = reader
        self._condition = condition
        self._buffer = buffer
        self._token = token

    @abstractmethod
    def action(self) -> None:
        pass
