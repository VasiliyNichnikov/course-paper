from abc import ABC, abstractmethod

from buffer import Buffer
from characterreader import CharacterReader
from conditions.typescondition import TypesCondition
from tokens.workingwithtoken import WorkingWithToken


class TransitionParent(ABC):
    def __init__(self, **kwargs) -> None:
        self._buffer: Buffer = kwargs["buffer"]
        self._reader: CharacterReader = kwargs["reader"]
        # self._checking_symbol: CheckingSymbol = kwargs["checking_symbol"] TODO нужно проверить дочерние классы
        self._token: WorkingWithToken = kwargs["token"]

    @abstractmethod
    def action(self) -> TypesCondition | bool:
        pass
