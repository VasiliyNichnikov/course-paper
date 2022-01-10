from typing import List

from buffer import Buffer
from config import name_token_file
from tokens.tablesoftokens import TablesOfTokens
from tokens.typesoftokentables import TypesOfTokenTables


class WorkingWithTokenException(Exception):
    pass


class TokenNotFound(WorkingWithTokenException):
    pass


class WorkingWithToken:
    def __init__(self, buffer: Buffer, tables: TablesOfTokens):
        self.__buffer = buffer
        self.__tables = tables

    def find_token_in_selected_table(self, t: TypesOfTokenTables) -> int:
        """
        Ищет лексему из буфера в выбранной таблице :param t: с возвращением номера лексемы в таблице
        :param t: Выбранная таблица
        :return: Возвращает номер лексемы в таблице
        """
        table = self.__tables.get_selected_table(t)
        string = self.__buffer.get_combined_characters()
        for index in range(len(table)):
            if table[index] == string:
                return index
        raise TokenNotFound("The token was not found in the table")

    def writing_token_to_table(self, t: TypesOfTokenTables):
        """
        Записывает лексему из буфера в выбранную таблицу t, если там не было этой лексемы
        :param t: Выбранная таблица
        :return: Возвращает номер данной лексеме в таблице, если же лексема уже есть в таблице, возвращает -1 # TODO это может не совсем корректный результат
        """
        table = self.__tables.get_selected_table(t)
        string = self.__buffer.get_combined_characters()
        token_exists_in_table = self.__check_if_token_exists_in_table(table, string)
        if not token_exists_in_table:
            id_element = self.__tables.add_element_to_selected_table(t, string) - 1
            return id_element
        return -1

    @staticmethod
    def writing_to_token_file(n, k) -> None:
        """
        Записывает пару чисел в файл лексем
        :param n: Номер таблицы (от 1 до 4)
        :param k: Номер лексемы в этой таблице
        :return: Ничего не возвращает
        """
        with open(name_token_file, 'a', encoding="UTF-8") as file:
            data = f"({n}, {k})"
            file.write(data)

    @staticmethod
    def __check_if_token_exists_in_table(table: List[str], token: str) -> bool:
        for item in table:
            if item == token:
                return True
        return False
