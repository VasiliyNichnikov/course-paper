from typing import List


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

    def add_id(self, ID: str) -> None:
        self.__ids.append(ID)

    def add_number(self, number: str) -> None:
        self.__numbers.append(number)
