from lexicalanalyzer.conditions.typescondition import TypesCondition


class Condition:
    def __init__(self) -> None:
        self.__now = TypesCondition.H

    @property
    def now(self) -> TypesCondition:
        return self.__now

    @now.setter
    def now(self, value: TypesCondition) -> None:
        self.__now = value
