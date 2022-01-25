from typing import List

from config import TOKEN_FILE
from lexicalanalyzer.buffer import Buffer
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
        self.__z = 0

    @property
    def z(self) -> int:
        return self.__z

    def find_token_in_selected_table(self, t: TypesOfTokenTables) -> int:
        """
        Ищет лексему из буфера в выбранной таблице :param t: с возвращением номера лексемы в таблице
        :param t: Выбранная таблица
        :return: Возвращает номер лексемы в таблице, если лексемы нет, возвращает -1
        """
        table = self.__tables.get_selected_table(t)
        string = self.__buffer.get_combined_characters()
        for index in range(len(table)):
            if table[index] == string:
                self.__z = index
                return index
        self.__z = -1
        return self.__z

    def writing_token_to_table(self, t: TypesOfTokenTables) -> int:
        """
        Записывает лексему из буфера в выбранную таблицу t, если там не было этой лексемы
        :param t: Выбранная таблица
        :return: Возвращает номер данной лексеме в таблице, если же лексема уже есть в таблице, возвращает -1 # TODO это может не совсем корректный результат
        """
        table = self.__tables.get_selected_table(t)
        string = self.__buffer.get_combined_characters()
        token_exists_in_table, index = self.__check_if_token_exists_in_table(table, string)
        # print(f"String - {string}; Token in table - {token_exists_in_table}")
        if not token_exists_in_table:
            id_element = self.__tables.add_element_to_selected_table(t, string) - 1
            self.__z = id_element
            return id_element
        else:
            self.__z = index
        return self.__z

    def writing_token_to_file(self, t: TypesOfTokenTables, k) -> None:
        """
        Записывает пару чисел в файл лексем
        :param t: Тип таблицы
        :param k: Номер лексемы в этой таблице
        :return: Ничего не возвращает
        """
        self.__tables.add_element_to_selected_table(TypesOfTokenTables.TOKENS, (t.value, k))
        with open(TOKEN_FILE, 'a', encoding="UTF-8") as file:
            data = f"({t.value}, {k})"
            file.write(data)

    @staticmethod
    def __check_if_token_exists_in_table(table: List[str], token: str) -> (bool, int):
        for i in range(len(table)):
            if table[i] == token:
                return True, i
        return False, -1
