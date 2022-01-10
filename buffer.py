from typing import List, Any


class Buffer:
    def __init__(self):
        self.__data: List = []

    def add(self, element: Any) -> None:
        self.__data.append(element)

    def clear(self) -> None:
        self.__data.clear()
