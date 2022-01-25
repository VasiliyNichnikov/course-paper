from abc import abstractmethod, ABC

from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.conditions.condition import Condition
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
