class CheckingSymbolException(Exception):
    pass


class StringHasMoreThanOneLetter(CheckingSymbolException):
    pass


class CheckingSymbol:
    @staticmethod
    def is_value_letter(value: str) -> bool:
        """
        Проверяет, является ли значение буквой
        :param value: Значение, который нужно проверить
        :return: Возвращает true, если значение является буквой, в противном случае false
        """
        if len(value) > 1:
            raise StringHasMoreThanOneLetter(f"A string ({value}) has more than one letter")
        return value.isalpha()

    @staticmethod
    def is_value_number(value: str) -> bool:
        """
        Проверяет, является ли значение цифрой
        :param value: Значение, который нужно проверить
        :return: Возвращает true, если значение является числом, в противном случае false
        """
        if len(value) > 1:
            raise StringHasMoreThanOneLetter(f"A string ({value}) has more than one letter")
        return value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def check_hex(self, value: str) -> bool:
        """
        Проверяет, является ли значение цифрой или буквой из диапазона A..F или a..f
        :param value: Значение, которое нужно проверить
        :return: Возвращает true, если переданное значение является цифрой или буквой из диапазона A..F или a..f
        """
        if len(value) > 1:
            raise StringHasMoreThanOneLetter(f"A string ({value}) has more than one letter")
        return self.is_value_number(value) or self.__value_is_in_range_A_F_or_a_f(value)

    def check_AFH(self, value: str) -> bool:
        """
        Проверяет, является ли значение буквой из диапазона A..F и a..f или буквой H, h
        :param value: Значение, которое нужно проверить
        :return: Возвращает true, если переданное значение является буквой из диапазона A..F и a..f или буквой H, h
        """
        if len(value) > 1:
            raise StringHasMoreThanOneLetter(f"A string ({value}) has more than one letter")
        return self.__value_is_in_range_A_F_or_a_f(value) or value in ['H', 'h']

    @staticmethod
    def __value_is_in_range_A_F_or_a_f(value: str) -> bool:
        return value in ['A', 'B', 'C', 'D', 'E', 'F',
                         'a', 'b', 'c', 'd', 'e', 'f']
