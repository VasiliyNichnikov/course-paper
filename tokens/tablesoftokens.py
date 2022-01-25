from typing import List, Tuple

from tokens.typesoftokentables import TypesOfTokenTables


class TablesOfTokens:
    def __init__(self) -> None:
        self.__service: List[str] = ["readln",  # 0
                                     "writeln",  # 1
                                     "if",  # 2
                                     "else",  # 3
                                     "for",  # 4
                                     "to",  # 5
                                     "while",  # 6
                                     "true",  # 7
                                     "false",  # 8
                                     "end",  # 9
                                     "int",  # 10
                                     "float",  # 11
                                     "bool",  # 12
                                     "begin",  # 13
                                     "next",  # 14
                                     "step"  # 15
                                     ]
        self.__limiters: List[str] = ['!',  # 0
                                      ',',  # 1
                                      ';',  # 2
                                      ':',  # 3
                                      '(',  # 4
                                      ')',  # 5
                                      '+',  # 6
                                      '-',  # 7
                                      '*',  # 8
                                      '/',  # 9
                                      '==',  # 10
                                      "!=",  # 11
                                      '>',  # 12
                                      '<',  # 13
                                      "<=",  # 14
                                      ">=",  # 15
                                      "(*",  # 16
                                      "*)",  # 17
                                      "||",  # 18
                                      "&&",  # 19
                                      "!",  # 20
                                      ":=",  # 21
                                      "\n"  # 22
                                      ]
        self.__ids: List[str] = []
        self.__numbers: List[str] = []
        self.__tokens: List[Tuple] = []

        self.__tables = {
            TypesOfTokenTables.SERVICE.value: self.__service,
            TypesOfTokenTables.LIMITERS.value: self.__limiters,
            TypesOfTokenTables.IDS.value: self.__ids,
            TypesOfTokenTables.NUMBERS.value: self.__numbers,
            TypesOfTokenTables.TOKENS.value: self.__tokens
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

    @property
    def tokens(self) -> List[Tuple]:
        return self.__tokens

    def get_selected_table(self, t: TypesOfTokenTables | int) -> List[str]:
        index = t
        if isinstance(t, TypesOfTokenTables):
            index = t.value
        table = self.__tables[index]
        return table.copy()

    def add_element_to_selected_table(self, t: TypesOfTokenTables, element: str | Tuple) -> int:
        self.__tables[t.value].append(element)
        return len(self.__tables[t.value])
