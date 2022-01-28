from abc import ABC, abstractmethod

from syntaxanalyzer.syntaxerrors import *
from tokens.controllertokens import ControllerTokens


class ConditionParent(ABC):
    def __init__(self, ct: ControllerTokens) -> None:
        self._ct = ct

    @abstractmethod
    def action(self) -> None:
        pass


class Program(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        body = Body(self._ct)
        body.action()


class Body(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)
        self.__end = False

    def action(self) -> None:
        self.__checking()
        if self.__end:
            return
        while self._ct.is_current_token_for_s([":", "\n"]):
            self._ct.reading_next_token()
            self.__checking()
            if self.__end:
                return

    def __checking(self) -> None:
        transition: ConditionParent | None = None
        if self._ct.is_current_token_for_s(["int", "bool", "float"]):
            self._ct.reading_next_token()
            transition = ID(self._ct)
        elif self._ct.is_token_id() \
                or self._ct.is_current_token_for_s(["if", "for", "while", "begin", "writeln", "readln"]):
            transition = Operator(self._ct)
        elif self._ct.is_current_token_for_s("end"):
            print("Программа написана корректна")
            self.__end = True
            return

        if transition is None:
            raise BodyError("ошибка в теле программы", self._ct.token_preview)
        else:
            transition.action()


class ID(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_token_id():
            self._ct.reading_next_token()
            while self._ct.is_current_token_for_s(","):
                self._ct.reading_next_token()
                if self._ct.is_token_id():
                    self._ct.reading_next_token()
                else:
                    raise IDError("не верно объявлен идентификатор", self._ct.token_preview)


class Operator(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        transition: ConditionParent | None = None
        if self._ct.is_token_id():
            transition = Assignments(self._ct)
        elif self._ct.is_current_token_for_s("begin"):
            transition = Composite(self._ct)
        elif self._ct.is_current_token_for_s("if"):
            transition = Conditional(self._ct)
        elif self._ct.is_current_token_for_s("for"):
            transition = FixedCycle(self._ct)
        elif self._ct.is_current_token_for_s("while"):
            transition = ConditionCycle(self._ct)
        elif self._ct.is_current_token_for_s("writeln"):
            transition = Entry(self._ct)
        elif self._ct.is_current_token_for_s("readln"):
            transition = Conclusion(self._ct)

        if transition is None:
            raise OperatorError("не верно обработан оператор", self._ct.token_preview)
        else:
            self._ct.reading_next_token()
            transition.action()


class Composite(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__checking()
        while self._ct.is_current_token_for_s(";"):
            self._ct.reading_next_token()
            self.__checking()
        if self._ct.is_current_token_for_s("end"):
            self._ct.reading_next_token()
        else:
            raise CompositeError("не верно обработан составной оператор", self._ct.token_preview)

    def __checking(self) -> None:
        if self._ct.is_token_id() \
                or self._ct.is_current_token_for_s(["if", "for", "while", "begin", "writeln", "readln"]):
            operator = Operator(self._ct)
            operator.action()
        else:
            raise CompositeError("не верно обработан составной оператор", self._ct.token_preview)


class Assignments(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_current_token_for_s(":="):
            self._ct.reading_next_token()
            expression = Expression(self._ct)
            expression.action()
        else:
            raise AssignmentsError("не верно обработано выражение", self._ct.token_preview)


class Expression(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__transition_operand()
        while self._ct.is_current_token_for_s(["!=", "==", "<", "<=", ">", ">="]):
            self._ct.reading_next_token()
            self.__transition_operand()

    def __transition_operand(self) -> None:
        operand = Operand(self._ct)
        operand.action()


class Operand(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__transition_summand()
        while self._ct.is_current_token_for_s(["+", "-", "||"]):
            self._ct.reading_next_token()
            self.__transition_summand()

    def __transition_summand(self) -> None:
        summand = Summand(self._ct)
        summand.action()


class Summand(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__transition_multiplier()
        while self._ct.is_current_token_for_s(["*", "/", "&&"]):
            self._ct.reading_next_token()
            self.__transition_multiplier()

    def __transition_multiplier(self) -> None:
        multiplier = Multiplier(self._ct)
        multiplier.action()


class Multiplier(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_token_id() \
                or self._ct.is_token_number() \
                or self._ct.is_current_token_for_s(["true", "false"]):
            self._ct.reading_next_token()
        elif self._ct.is_current_token_for_s("!"):
            self._ct.reading_next_token()
            multiplier = Multiplier(self._ct)
            multiplier.action()
        elif self._ct.is_current_token_for_s("("):
            self._ct.reading_next_token()
            expression = Expression(self._ct)
            expression.action()
            if self._ct.is_current_token_for_s(")"):
                self._ct.reading_next_token()
            else:
                raise MultiplierError("не верно обработан множитель", self._ct.token_preview)
        else:
            raise MultiplierError("не верно обработан множитель", self._ct.token_preview)


class Conditional(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_current_token_for_s("("):
            self._ct.reading_next_token()
            expression = Expression(self._ct)
            expression.action()
            if self._ct.is_current_token_for_s(")"):
                self._ct.reading_next_token()
                self.__transition_operator()
                while self._ct.is_current_token_for_s("else"):
                    self._ct.reading_next_token()
                    self.__transition_operator()
            else:
                raise ConditionalError("не верно обработан условный оператор", self._ct.token_preview)
        else:
            raise ConditionalError("не верно обработан условный оператор", self._ct.token_preview)

    def __transition_operator(self) -> None:
        operator = Operator(self._ct)
        operator.action()


class FixedCycle(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_token_id():
            self._ct.reading_next_token()
            assignments = Assignments(self._ct)
            assignments.action()
            if self._ct.is_current_token_for_s("to"):
                self._ct.reading_next_token()
                self.__transition_expression()
                while self._ct.is_current_token_for_s("step"):
                    self._ct.reading_next_token()
                    self.__transition_expression()
                operator = Operator(self._ct)
                operator.action()
                if self._ct.is_current_token_for_s("next"):
                    self._ct.reading_next_token()
                else:
                    raise FixedCycleError("не верно обработан фиксированный цикл", self._ct.token_preview)
            else:
                raise FixedCycleError("не верно обработан фиксированный цикл", self._ct.token_preview)
        else:
            raise FixedCycleError("не верно обработан фиксированный цикл", self._ct.token_preview)

    def __transition_expression(self) -> None:
        expression = Expression(self._ct)
        expression.action()


class ConditionCycle(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_current_token_for_s("("):
            self._ct.reading_next_token()
            expression = Expression(self._ct)
            expression.action()
            if self._ct.is_current_token_for_s(")"):
                self._ct.reading_next_token()
            else:
                raise ConditionCycleError("не верно обработан условный цикл", self._ct.token_preview)
        else:
            raise ConditionCycleError("не верно обработан условный цикл", self._ct.token_preview)


class Entry(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__checking()
        while self._ct.is_current_token_for_s(","):
            self._ct.reading_next_token()
            self.__checking()

    def __checking(self) -> None:
        if self._ct.is_token_id():
            self._ct.reading_next_token()
        else:
            raise EntryError("не верно обработан оператор ввода", self._ct.token_preview)


class Conclusion(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__transition_expression()
        while self._ct.is_current_token_for_s(","):
            self._ct.reading_next_token()
            self.__transition_expression()

    def __transition_expression(self) -> None:
        expression = Expression(self._ct)
        expression.action()
