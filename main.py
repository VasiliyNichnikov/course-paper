# from typing import
from states import States


class Main:
    def __init__(self, code_program: str) -> None:
        self.__state = States.CS
        self.__buffer: list = []
        self.__code_program = code_program
        self.__selected_symbol = code_program[0]

    def __scanner(self) -> bool:
        match self.__state:
            case States.H:
                while self.__selected_symbol == ' ' or self.__selected_symbol == '\n':
                    self.__reading_next_character()  # процедура считывания очередного символа текста в переменную self.__code_program

                if self.__is_string_letter():
                    self.__clear_buffer() # Очистка буфера
                    self.__add_selected_symbol_to_buffer() # Добавить выбранный символ в конец буфера
                    self.__reading_next_character()
                    self.__state = States.I
                elif self.__selected_symbol in ['0', '1']:
                    self.__clear_buffer()
                    self.__state = States.N2
                    self.__add_selected_symbol_to_buffer()
                    self.__reading_next_character()
                elif self.__selected_symbol in ['2', '3', '4', '5', '6', '7']:
                    self.__clear_buffer()
                    self.__selected_symbol = States.N8
                    self.__add_selected_symbol_to_buffer()
                    self.__reading_next_character()
                elif self.__selected_symbol in ['8', '9']:
                    self.__clear_buffer()
                    self.__selected_symbol = States.N10
                    self.__add_selected_symbol_to_buffer()
                    self.__reading_next_character()
                elif self.__selected_symbol == '.':
                    self.__clear_buffer()
                    self.__add_selected_symbol_to_buffer()
                    self.__reading_next_character()
                    self.__state = States.P1
                elif self.__selected_symbol == '/':
                    self.__reading_next_character()
                    self.__state = States.C1
                elif self.__selected_symbol == '<':
                    self.__reading_next_character()
                    self.__state = States.M1
                elif self.__selected_symbol == '>':
                    self.__reading_next_character()
                    self.__state = States.M2
                elif self.__selected_symbol == '}':
                    # out(n, k) - процедура записи пары чисел (n, k) в файл лексем
                    self.__state = States.V
                else:
                    self.__state = States.OG

            case States.I:
                while self.__is_string_letter() or self.__is_string_number():
                    # Добавляем очередной символ в конец буфера S
                    self.__reading_next_character()
                # look(t) Вызов функции, которая ищет лексему из буфера S в таблице t с возвращением номера лексемы в таблице

            case States.N2:
                pass

            case States.N8:
                pass

            case States.N10:
                pass

            case States.N16:
                pass

            case States.B:
                pass

            case States.O:
                pass

            case States.D:
                pass

            case States.HX:
                pass

            case States.E11:
                pass

            case States.ZN:
                pass

            case States.E12:
                pass

            case States.E13:
                pass

            case States.P1:
                pass

            case States.P2:
                pass

            case States.E21:
                pass

            case States.E22:
                pass

            case States.C1:
                pass

            case States.C2:
                pass

            case States.C3:
                pass

            case States.M1:
                pass

            case States.M2:
                pass

            case States.OG:
                pass

    def __reading_next_character(self) -> None:
        self.__code_program = self.__code_program[1:]
        self.__selected_symbol = self.__code_program[0]

    def __is_string_letter(self) -> bool:
        pass

    def __add_selected_symbol_to_buffer(self) -> None:
        self.__buffer.append(self.__selected_symbol)

    def __clear_buffer(self) -> None:
        self.__buffer.clear()

    def __is_string_number(self) -> bool:
        pass
