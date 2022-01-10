class WorkingWithNumberException(Exception):
    pass


class UnsupportedNumberSystemIsSpecified(WorkingWithNumberException):
    pass


class WorkingWithNumber:
    def __init__(self) -> None:
        self.__supported_number_systems = [2, 8, 16]

    def conversion_from_number_system_to_decimal(self, number: str,
                                                 base: int) -> int:  # TODO Переводит только int значение, нужно добавить для плавующих значений
        """
        Переводит число из СС по основанию base в десятичную СС
        :param number: Число в виде строки, которое нужно перевести в десятичную СС
        :param base: Основание числа
        :return: Возвращает число в десятичной СС
        """
        if base not in self.__supported_number_systems:
            raise UnsupportedNumberSystemIsSpecified(f"This number system ({base}) is not supported")

        len_number = len(number)
        result: int = 0
        for index in range(len_number):
            degree = len_number - index - 1
            result += self.__check_hexadecimal_symbol_system(number[index]) * base ** degree
        return result

    @staticmethod
    def converting_from_string_to_decimal_form(number: str) -> float:
        """
        Преобразование действительного числа из строковой формы записи в десятичную форму
        :param number: Число, которое нужно преобразовать
        :return: Возвращает число в десятичной форме
        """
        return float(number)

    @staticmethod
    def __check_hexadecimal_symbol_system(symbol: str) -> int:
        match symbol.upper():
            case 'A':
                return 10
            case 'B':
                return 11
            case 'C':
                return 12
            case 'D':
                return 13
            case 'E':
                return 14
            case 'F':
                return 15
        return int(symbol)

# c = WorkingWithNumber()
# print(c.conversion_from_number_system_to_decimal("3BC9", 16))
