from typing import Tuple


class SyntaxErrors(Exception):
    def __init__(self, message_error: str, token: Tuple) -> None:
        self.__body_error = f"Синтаксическая ошибка: {message_error}; Ошибочный токен: {token}"
        super().__init__(self.__body_error)


class BodyError(SyntaxErrors):
    pass


class IDError(SyntaxErrors):
    pass


class OperatorError(SyntaxErrors):
    pass


class CompositeError(SyntaxErrors):
    pass


class AssignmentsError(SyntaxErrors):
    pass


class ExpressionError(SyntaxErrors):
    pass


class OperandError(SyntaxErrors):
    pass


class SummandError(SyntaxErrors):
    pass


class MultiplierError(SyntaxErrors):
    pass


class ConditionalError(SyntaxErrors):
    pass


class FixedCycleError(SyntaxErrors):
    pass


class ConditionCycleError(SyntaxErrors):
    pass


class EntryError(SyntaxErrors):
    pass


class ConclusionError(SyntaxErrors):
    pass

