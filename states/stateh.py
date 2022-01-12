from buffer import Buffer
from characterreader import CharacterReader
from checkingsymbol import CheckingSymbol
from states.stateparent import StateParent
from tokens.workingwithtoken import WorkingWithToken


class StateH(StateParent):

    def __init__(self, reader: CharacterReader, checking_symbol: CheckingSymbol, buffer: Buffer,
                 token: WorkingWithToken):
        super().__init__(reader, checking_symbol, buffer, token)

    def action(self) -> None:
        self.__cleaning_from_code()
        self.__transition_to_id()
        self.__transition_to_binary_notation()
        self.__transition_to_octal_notation()
        self.__transition_to_decimal_notation()
        self.__transition_to_point()
        self.__transition_to_slash()
        self.__transition_to_less()
        self.__transition_to_more()
        self.__transition_to_closing_curly_brace()
        self.__transition_to_limiter()

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in [' ', '\n']:
            self._reader.trip_first_character()

    # def __transition_to_id(self) -> None:
    #     if not self._checking_symbol.is_value_letter(self._reader.selected_symbol):
    #         return
    #     self.__reading_next_character_and_clearing_buffer()
        # TODO поменять состояние и по сути завершить работу данного класса

    # def __transition_to_binary_notation(self) -> bool:
    #     if self._reader.selected_symbol not in ['0', '1']:
    #         return False
    #     self._buffer.clear()
    #     # TODO перход в новое состояние (двоичную систему счисления)
    #     self._buffer.add(self._reader.selected_symbol)
    #     self._reader.trip_first_character()
    #     return True

    # def __transition_to_octal_notation(self) -> bool:
    #     if self._reader.selected_symbol not in ['2', '3', '4', '5', '6', '7']:
    #         return False
    #     self._buffer.clear()
    #     # TODO перход в новое состояние (восьмеричную систему счисления)
    #     self._buffer.add(self._reader.selected_symbol)
    #     self._reader.trip_first_character()
    #     return True

    # def __transition_to_decimal_notation(self) -> bool:
    #     if self._reader.selected_symbol not in ['8', '9']:
    #         return False
    #     self._buffer.clear()
    #     # TODO перход в новое состояние (десятичную систему счисления)
    #     self._buffer.add(self._reader.selected_symbol)
    #     self._reader.trip_first_character()
    #     return True

    # def __transition_to_point(self) -> bool:
    #     if self._reader.selected_symbol != '.':
    #         return False
    #     self.__reading_next_character_and_clearing_buffer()
    #     # TODO поменять состояние и по сути завершить работу данного класса
    #     return True

    # def __transition_to_slash(self) -> bool:
    #     if self._reader.selected_symbol != '/':
    #         return False
    #     self.__reading_next_character_and_clearing_buffer()
    #     # TODO поменять состояние и по сути завершить работу данного класса
    #     return True

    # def __transition_to_less(self) -> bool:
    #     if self._reader.selected_symbol != '<':
    #         return False
    #     self.__reading_next_character_and_clearing_buffer()
    #     # TODO поменять состояние и по сути завершить работу данного класса
    #     return True

    # def __transition_to_more(self) -> bool:
    #     if self._reader.selected_symbol != '>':
    #         return False
    #     self.__reading_next_character_and_clearing_buffer()
    #     # TODO поменять состояние и по сути завершить работу данного класса
    #     return True

    # def __transition_to_closing_curly_brace(self) -> bool:
    #     if self._reader.selected_symbol != '}':
    #         return False
    #     self._token.writing_to_token_file(2, 2)
    #     self.__reading_next_character_and_clearing_buffer()
    #     # TODO поменять состояние и по сути завершить работу данного класса
    #     return True

    # def __transition_to_limiter(self) -> bool:
    #     # TODO в противном случае, если состояние не поменялось ни на одном из методом, меняем его на ограничитель
    #     # TODO переход в новое состояние
    #     return True

    # def __reading_next_character_and_clearing_buffer(self) -> None:
    #     self._buffer.clear()
    #     self._buffer.add(self._reader.selected_symbol)
    #     self._reader.trip_first_character()
