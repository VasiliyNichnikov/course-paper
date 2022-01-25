from typing import Tuple, List

from tokens.tablesoftokens import TablesOfTokens
from tokens.typesoftokentables import TypesOfTokenTables


class ControllerTokens:
    __token_now: Tuple = None

    def __init__(self, tables: TablesOfTokens) -> None:
        self.__tables: TablesOfTokens = tables
        self.reading_next_token()

    def reading_next_token(self) -> None:
        self.__token_now: Tuple = self.__tables.tokens[0]
        self.__tables.tokens.pop(0)

    def is_current_token_for_s(self, s: str) -> bool:
        number_table, number_element = self.__token_now
        selected_table = self.__get_selected_table(number_table, number_element)
        return selected_table[number_table] == s

    def is_token_id(self) -> bool:
        number_table = self.__token_now[0]
        selected_table = self.__tables.get_selected_table(number_table)
        return selected_table == TypesOfTokenTables.IDS.value

    def is_token_number(self) -> bool:
        number_table = self.__token_now[0]
        selected_table = self.__tables.get_selected_table(number_table)
        return selected_table == TypesOfTokenTables.NUMBERS.value

    def __get_selected_table(self, number_table: int, index_element: int) -> List[str]:
        selected_table = self.__tables.get_selected_table(number_table)
        if 0 > index_element >= len(selected_table):
            raise IndexError("the token has gone out of the array")
        return selected_table


