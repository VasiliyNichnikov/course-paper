from typing import List

from tokens.typesoftokentables import TypesOfTokenTables


class TablesOfTokens:
    def __init__(self) -> None:
        self.__service: List[str] = ["read", "write", "if",
                                     "then", "else", "for",
                                     "to", "while", "do",
                                     "true", "false", "or",
                                     "and", "not", "as"]
        self.__limiters: List[str] = ['{', '}', '%',
                                      '!', '$', ',',
                                      ';', '[', ']',
                                      ':', '(', ')',
                                      '+', '-', '*',
                                      '/', '=', "<>",
                                      '>', '<', "<=",
                                      ">=", "/*", "*/"]
        self.__ids: List[str] = []
        self.__numbers: List[str] = []
        self.__tables = {
            TypesOfTokenTables.SERVICE: self.__service,
            TypesOfTokenTables.LIMITERS: self.__limiters,
            TypesOfTokenTables.IDS: self.__ids,
            TypesOfTokenTables.NUMBERS: self.__numbers
        }

    @property
    def service(self) -> List[str]:
        return self.__service

    @property
    def limiters(self) -> List[str]:
        return self.__limiters

    @property
    def ids(self) -> List[str]:
        return self.__ids

    @property
    def numbers(self) -> List[str]:
        return self.__numbers

    def get_selected_table(self, t: TypesOfTokenTables) -> List[str]:
        table = self.__tables[t]
        return table.copy()

    def add_element_to_selected_table(self, t: TypesOfTokenTables, element: str) -> int:
        self.__tables[t].append(element)
        return len(self.__tables[t])
