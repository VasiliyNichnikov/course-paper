from abc import ABC, abstractmethod

from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from states.typesstate import TypesState
from tokens.workingwithtoken import WorkingWithToken


class TransitionParent(ABC):
    def __init__(self, **kwargs) -> None:
        self._buffer: Buffer = kwargs["buffer"]
        self._reader: CharacterReader = kwargs["reader"]
        self._checking_symbol: CheckingSymbol = kwargs["checking_symbol"]
        self._token: WorkingWithToken = kwargs["token"]

    @abstractmethod
    def action(self) -> TypesState | bool:
        pass
