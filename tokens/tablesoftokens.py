from typing import List

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
