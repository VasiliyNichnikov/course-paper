from abc import ABC, abstractmethod

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
        if self._ct.is_current_token_for_s("end") is False:
            print("Error Program")  # TODO error


class Body(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__checking()
        while self._ct.is_current_token_for_s(":") or self._ct.is_current_token_for_s("/n"):
            self.__checking()

    def __checking(self) -> None:
        transition: ConditionParent | None = None
        if self._ct.is_current_token_for_s("int") \
                or self._ct.is_current_token_for_s("bool") \
                or self._ct.is_current_token_for_s("float"):
            transition = ID(self._ct)
        elif self._ct.is_current_token_for_s(":=") \
                or self._ct.is_current_token_for_s("if") \
                or self._ct.is_current_token_for_s("for") \
                or self._ct.is_current_token_for_s("while") \
                or self._ct.is_current_token_for_s("begin") \
                or self._ct.is_current_token_for_s("writeln") \
                or self._ct.is_current_token_for_s("readln"):
            transition = Operator(self._ct)
        if transition is None:
            print("Error Body")  # TODO Error
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
                    print("Error ID")  # TODO Error


class Operator(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        transition: ConditionParent | None = None
        if self._ct.is_token_id():
            # self._ct.reading_next_token()
            transition = Assignments(self._ct)
        elif self._ct.is_current_token_for_s("begin"):
            # self._ct.reading_next_token()
            transition = Composite(self._ct)
        elif self._ct.is_current_token_for_s("if"):
            # self._ct.reading_next_token()
            transition = Conditional(self._ct)
        elif self._ct.is_current_token_for_s("for"):
            # self._ct.reading_next_token()
            transition = FixedCycle(self._ct)
        elif self._ct.is_current_token_for_s("while"):
            # self._ct.reading_next_token()
            transition = ConditionCycle(self._ct)
        elif self._ct.is_current_token_for_s("writeln"):
            # self._ct.reading_next_token()
            transition = Entry(self._ct)
        elif self._ct.is_current_token_for_s("readln"):
            # self._ct.reading_next_token()
            transition = Conclusion(self._ct)

        if transition is None:
            print("Error Operator")  # TODO Error
        else:
            self._ct.reading_next_token()
            transition.action()


class Composite(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__checking()
        while self._ct.is_current_token_for_s(";"):
            self.__checking()
        if self._ct.is_current_token_for_s("end"):
            self._ct.reading_next_token()
        else:
            print("Error Composite 1")  # TODO Error

    def __checking(self) -> None:
        if self._ct.is_current_token_for_s(":=") \
                or self._ct.is_current_token_for_s("if") \
                or self._ct.is_current_token_for_s("for") \
                or self._ct.is_current_token_for_s("while") \
                or self._ct.is_current_token_for_s("begin") \
                or self._ct.is_current_token_for_s("writeln") \
                or self._ct.is_current_token_for_s("readln"):
            operator = Operator(self._ct)
            operator.action()
        else:
            print("Error Composite 2")  # TODO Error


class Assignments(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        if self._ct.is_current_token_for_s(":="):
            self._ct.reading_next_token()
            expression = Expression(self._ct)
            expression.action()
        else:
            print("Error Assignments")  # TODO Error


class Expression(ConditionParent):
    def __init__(self, ct: ControllerTokens) -> None:
        super().__init__(ct)

    def action(self) -> None:
        self.__transition_operand()
        while self._ct.is_current_token_for_s("!=") \
                or self._ct.is_current_token_for_s("==") \
                or self._ct.is_current_token_for_s("<") \
                or self._ct.is_current_token_for_s("<=") or self._ct.is_current_token_for_s(">") \
                or self._ct.is_current_token_for_s(">="):
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
        while self._ct.is_current_token_for_s("+") \
                or self._ct.is_current_token_for_s("-") \
                or self._ct.is_current_token_for_s("||"):
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
        while self._ct.is_current_token_for_s("*") \
                or self._ct.is_current_token_for_s("/") \
                or self._ct.is_current_token_for_s("&&"):
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
                or self._ct.is_current_token_for_s("true") \
                or self._ct.is_current_token_for_s("false"):
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
                print("Error Multiplier 1")  # TODO Error
        else:
            print("Error Multiplier 2")  # TODO Error


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
                self.__transition_operand()
                while self._ct.is_current_token_for_s("else"):
                    self._ct.reading_next_token()
                    self.__transition_operand()
            else:
                print("Error Conditional 1")  # TODO Error
        else:
            print("Error Conditional 2")  # TODO Error

    def __transition_operand(self) -> None:
        operand = Operand(self._ct)
        operand.action()


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
                    print("Error FixedCycle 1")  # TODO Error
            else:
                print("Error FixedCycle 2")  # TODO Error
        else:
            print("Error FixedCycle 3")  # TODO Error

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
                print("Error ConditionCycle 1")  # TODO Error
        else:
            print("Error ConditionCycle 2")  # TODO Error


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
            print("Error Entry 1")  # TODO Error


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
