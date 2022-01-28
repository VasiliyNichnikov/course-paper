from typing import NoReturn


class CharacterReaderException(Exception):
    pass


class ArrayOverflowError(CharacterReaderException):
    pass


class CharacterReader:
    def __init__(self, code: str) -> None:
        self.__code = code
        self.__selected_symbol = self.__code[0]

    @property
    def selected_symbol(self) -> str:
        """
        :return: Возвращает выбранный символ
        """
        return self.__selected_symbol

    def trip_first_character(self) -> NoReturn:
        """
        Обрезает первый символ из всей строки
        :return:
        """
        if len(self.__code) > 1:
            self.__code = self.__code[1:]
            self.__selected_symbol = self.__code[0]
        else:
            raise ArrayOverflowError("An array overflow has occurred")
