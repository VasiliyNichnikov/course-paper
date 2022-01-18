from typing import final

# Первая цифра варианта (2)
# Операция группы "Отношение"
UNEQUAL: final = "!="
EQUAL: final = "=="
LESS: final = "<"
LESS_THAN_OR_EQUAL_TO: final = "<="
GREATER_THAN: final = ">"
GREATER_THAN_ORE_EQUAL_TO: final = ">="

# Операция группы "Сложения"
ADDITION: final = "+"
SUBTRACTION: final = "-"
DISJUNCTION: final = "||"

# Операция группы "Умножение"
MULTIPLICATION: final = "*"
DIVISION: final = "/"
CONJUNCTION: final = "&&"

# Унарная операция
UNARY_OPERATION: final = "!"

# Вторая цифра варианта (3)
# Структура программы
START_OF_PROGRAM: final = ""
END_OF_PROGRAM: final = "end"
END_OF_LINE_CHARACTER: final = (":", "\n")

# Третья цифра варианта (3) Данный вариант совпадает с синтаксисом препода
# Синтаксис команд описания данных


# Четвертая цифра варианта (3)
# Описание типов данных
WHOLE: final = "int"
VALID: final = "float"
LOGICAL: final = "bool"

# Пятая цифра варианта (2)
# Синтаксис составного оператора
OPERATOR_START_WORD: final = "begin"
OPERATOR_END_WORD: final = "end"
SYMBOL_BETWEEN_OPERATORS: final = ";"
# Синтаксис оператора присваивания
ASSIGNMENT: final = ":="

# Синтаксис оператора условного перехода
CONDITION_TRANSITION_START: final = "("
CONDITION_TRANSITION_END: final = ")"

# Синтаксис оператора цикла с фиксированным числом повторений
END_OF_CYCLE_WITH_FIXED_REPETITION: final = "next"
MOVE_TO_NEXT_EXPRESSION: final = "step"

# Синтаксис условного оператора цикла
CONDITION_TRANSITION_CYCLE_START: final = "("
CONDITION_TRANSITION_CYCLE_END: final = ")"

# Синтаксис оператора ввода
INPUT_KEYWORD: final = "readln"

# Синтаксис оператора вывода
OUTPUT_KEYWORD: final = "writeln"

# Шестая цифра варианта (3)
# Многострочные комментарии в программе
BEGINNING_OF_COMMENT: final = "(*"
END_OF_COMMENT: final = "*)"
