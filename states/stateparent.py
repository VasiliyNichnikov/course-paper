from abc import abstractmethod, ABC

from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from tokens.workingwithtoken import WorkingWithToken


class StateParent(ABC):
    def __init__(self, reader: CharacterReader, checking_symbol: CheckingSymbol, buffer: Buffer,
                 token: WorkingWithToken) -> None:
        self._reader = reader
        self._checking_symbol = checking_symbol
        self._buffer = buffer
        self._token = token

    @abstractmethod
    def action(self) -> None:
        pass
