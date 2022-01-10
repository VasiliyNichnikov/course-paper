from typing import List, Any


class Buffer:
    def __init__(self):
        self.__data: List = []

    @property
    def data(self) -> List:
        return self.__data.copy()

    def get_combined_characters(self) -> str:
        return ''.join(self.__data)

    def add(self, element: Any) -> None:
        self.__data.append(element)

    def clear(self) -> None:
        self.__data.clear()
