from abc import abstractmethod, ABC

from lexicalanalyzer.typescondition import TypesCondition
from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader, ArrayOverflowError
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.condition import Condition
from myutils import reading_next_character, converting_numbers_writing_to_tokens, \
    converting_string_to_numbers_writing_to_tokens, cleaning_buffer_reading_next_character
from tokens.typesoftokentables import TypesOfTokenTables
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


class ConditionAnd(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '&':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H


class ConditionAssignment(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '=':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H


class ConditionB(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.check_hex(self._reader.selected_symbol):
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            converting_numbers_writing_to_tokens(self._buffer, self._token, 2)
            self._condition.now = TypesCondition.H


class ConditionC1(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '*':
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.C2
        else:
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 4)
            self._condition.now = TypesCondition.H


class ConditionC2(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__clearing_from_code()
        self._reader.trip_first_character()
        self._condition.now = TypesCondition.C3

    def __clearing_from_code(self) -> None:
        while self._reader.selected_symbol != '*':
            self._reader.trip_first_character()


class ConditionC3(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == ')':
            self._reader.trip_first_character()
            if self._reader.selected_symbol == '\n':
                self._reader.trip_first_character()
            self._condition.now = TypesCondition.H
        else:
            self._condition.now = TypesCondition.C2


class ConditionD(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.check_hex(self._reader.selected_symbol):
            self._condition.now = TypesCondition.N16
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._token.writing_token_to_table(TypesOfTokenTables.NUMBERS)
            self._token.writing_token_to_file(TypesOfTokenTables.NUMBERS, self._token.z)
            self._condition.now = TypesCondition.H


class ConditionE11(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_number(self._reader.selected_symbol) \
                or checking_symbol.is_value_letter(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.E12
        elif self._reader.selected_symbol in ['+', '-']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.ZN
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.check_hex(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N16
        else:
            self._condition.now = TypesCondition.ER


class ConditionE12(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()

        self.__cleaning_from_code(checking_symbol)
        if checking_symbol.check_hex(self._reader.selected_symbol):
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            converting_string_to_numbers_writing_to_tokens(self._buffer, self._token)
            self._condition.now = TypesCondition.H

    def __cleaning_from_code(self, checking_symbol: CheckingSymbol) -> None:
        while checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)


class ConditionE13(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        self.__cleaning_from_code(checking_symbol)
        if checking_symbol.is_value_letter(self._reader.selected_symbol) or self._reader.selected_symbol == '.':
            self._condition.now = TypesCondition.ER
        else:
            converting_string_to_numbers_writing_to_tokens(self._buffer, self._token)
            self._condition.now = TypesCondition.H

    def __cleaning_from_code(self, checking_symbol: CheckingSymbol) -> None:
        while checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)


class ConditionE21(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition):
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['+', '-']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.ZN
        elif checking_symbol.is_value_number(self._reader.selected_symbol):
            self._condition.now = TypesCondition.E22
        else:
            self._condition.now = TypesCondition.ER


class ConditionE22(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        self.__cleaning_from_code(checking_symbol)
        if checking_symbol.is_value_number(self._reader.selected_symbol) or self._reader.selected_symbol == '.':
            self._condition.now = TypesCondition.ER
        else:
            converting_string_to_numbers_writing_to_tokens(self._buffer, self._token)
            self._condition.now = TypesCondition.H

    def __cleaning_from_code(self, checking_symbol: CheckingSymbol) -> None:
        while checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)


class ConditionEqually(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '=':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H


class ConditionH(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition):
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__cleaning_from_code()
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_letter(self._reader.selected_symbol):
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.I
        elif self._reader.selected_symbol in ['0', '1']:
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N2
        elif self._reader.selected_symbol in ['2', '3', '4', '5', '6', '7']:
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N8
        elif self._reader.selected_symbol in ['8', '9']:
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N10
        elif self._reader.selected_symbol == '.':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol == '(':
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.C1
        elif self._reader.selected_symbol == '<':
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.M1
        elif self._reader.selected_symbol == '>':
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.M2
        elif self._reader.selected_symbol == ':':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.ASSIGNMENT
        elif self._reader.selected_symbol == '=':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.EQUALLY
        elif self._reader.selected_symbol == '!':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.UNEQUAL
        elif self._reader.selected_symbol == '|':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.OR
        elif self._reader.selected_symbol == '&':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.AND
        else:
            self._condition.now = TypesCondition.OG

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in [' ']:
            self._reader.trip_first_character()


class ConditionHX(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_letter(self._reader.selected_symbol) \
                or checking_symbol.is_value_number(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            converting_numbers_writing_to_tokens(self._buffer, self._token, 16)
            self._condition.now = TypesCondition.H


class ConditionI(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        try:
            self.__cleaning_from_code()
            self.__search_token_in_service_table()

            if self._token.z != -1:
                self._token.writing_token_to_file(TypesOfTokenTables.SERVICE, self._token.z)
            else:
                self._token.writing_token_to_table(TypesOfTokenTables.IDS)
                self._token.writing_token_to_file(TypesOfTokenTables.IDS, self._token.z)
            self._condition.now = TypesCondition.H

        except ArrayOverflowError:
            if self._buffer.get_combined_characters() == "end":
                self.__search_token_in_service_table()
                if self._token.z != -1:
                    self._token.writing_token_to_file(TypesOfTokenTables.SERVICE, self._token.z)
                self._condition.now = TypesCondition.V
            else:
                self._condition.now = TypesCondition.ER

    def __cleaning_from_code(self) -> None:
        checking_symbol = CheckingSymbol()
        while checking_symbol.is_value_letter(self._reader.selected_symbol) or \
                checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)

    def __search_token_in_service_table(self) -> None:
        self._token.find_token_in_selected_table(TypesOfTokenTables.SERVICE)


class ConditionM1(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '=':
            self._reader.trip_first_character()
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 14)
        else:
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 13)
        self._condition.now = TypesCondition.H


class ConditionM2(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '=':
            self._reader.trip_first_character()
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 15)
        else:
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 12)
        self._condition.now = TypesCondition.H


class ConditionN2(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__cleaning_from_code()
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['2', '3', '4', '5', '6', '7']:
            self._condition.now = TypesCondition.N8
        elif self._reader.selected_symbol in ['8', '9']:
            self._condition.now = TypesCondition.N10
        elif self._reader.selected_symbol in ['A', 'a', 'C', 'c', 'F', 'f']:
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['E', 'e']:
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.E11
        elif self._reader.selected_symbol in ['D', 'd']:
            self._buffer.add(self._reader.selected_symbol)
            self._condition.now = TypesCondition.D
        elif self._reader.selected_symbol in ['O', 'o']:
            self._condition.now = TypesCondition.O
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif self._reader.selected_symbol == '.':
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol in ['B', 'b']:
            self._buffer.add(self._reader.selected_symbol)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.B
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._condition.now = TypesCondition.N10

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in ['0', '1']:
            reading_next_character(self._buffer, self._reader)


class ConditionN8(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        self.__cleaning_from_code()
        if self._reader.selected_symbol in ['8', '9']:
            self._condition.now = TypesCondition.N10
        elif self._reader.selected_symbol in ['A', 'a', 'B', 'b', 'C', 'c', 'F', 'f']:
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['E', 'e']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.E11
        elif self._reader.selected_symbol in ['D', 'd']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.D
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif self._reader.selected_symbol == '.':
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol in ['O', 'o']:
            self._buffer.add(self._reader.selected_symbol)
            self._condition.now = TypesCondition.O
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._condition.now = TypesCondition.N10

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in ['2', '3', '4', '5', '6', '7']:
            reading_next_character(self._buffer, self._reader)


class ConditionN10(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        self.__cleaning_from_code()
        if self._reader.selected_symbol in ['A', 'a', 'B', 'b', 'C', 'c', 'F', 'f']:
            self._condition.now = TypesCondition.N16
        elif self._reader.selected_symbol in ['E', 'e']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.E11
        elif self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        elif self._reader.selected_symbol == '.':
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol in ['D', 'd']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.D
        elif checking_symbol.is_value_letter(self._reader.selected_symbol):
            self._condition.now = TypesCondition.ER
        else:
            self._token.writing_token_to_table(TypesOfTokenTables.NUMBERS)
            self._token.writing_token_to_file(TypesOfTokenTables.NUMBERS, self._token.z)
            self._condition.now = TypesCondition.H

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in ['8', '9']:
            reading_next_character(self._buffer, self._reader)


class ConditionN16(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__cleaning_from_code()
        if self._reader.selected_symbol in ['H', 'h']:
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.HX
        else:
            self._condition.now = TypesCondition.ER

    def __cleaning_from_code(self) -> None:
        checking_symbol = CheckingSymbol()
        while checking_symbol.check_hex(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)


class ConditionO(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_letter(self._reader.selected_symbol) or checking_symbol.is_value_number(
                self._reader.selected_symbol):
            self._condition = TypesCondition.ER
        else:
            converting_numbers_writing_to_tokens(self._buffer, self._token, 8)
            self._condition.now = TypesCondition.H


class ConditionOG(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self._buffer.clear()
        self._buffer.add(self._reader.selected_symbol)
        self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)

        if self._token.z != -1:
            self._reader.trip_first_character()
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
            self._condition.now = TypesCondition.H
        else:
            self._condition.now = TypesCondition.ER


class ConditionOr(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '|':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H


class ConditionP1(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.P2
        else:
            self._condition.now = TypesCondition.ER


class ConditionP2(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__clearing_from_code()
        checking_symbol = CheckingSymbol()
        if self._reader.selected_symbol in ['E', 'e']:
            reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.E21
        elif checking_symbol.is_value_letter(self._reader.selected_symbol) or self._reader.selected_symbol == '.':
            self._condition.now = TypesCondition.ER
        else:
            converting_string_to_numbers_writing_to_tokens(self._buffer, self._token)
            self._condition.now = TypesCondition.H

    def __clearing_from_code(self) -> None:
        checking_symbol = CheckingSymbol()
        while checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)


class ConditionUnequally(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '=':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H


class ConditionZN(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_number(self._reader.selected_symbol):
            reading_next_character(self._buffer, self._reader)
            self._condition = TypesCondition.E13
        else:
            self._condition = TypesCondition.ER
