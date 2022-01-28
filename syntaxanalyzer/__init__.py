from syntaxanalyzer.conditions import Program

from syntaxanalyzer.syntaxerrors import SyntaxErrors
from tokens.controllertokens import ControllerTokens


# conclusion
# Переходим в expression (выражение)
# Запускаем цикл while и проверяем наличие в лексеме ","
# Во время работы цикла, переходим в expression (выражение)
# program:
# Переходим сразу в body
# После выхода, проверяем что последнее слово = "end"
# Если последнее слово != "end", выкидываем ошибку
# body:
# Если текущий токен равен int, bool, float, то переходим в id
# Если текущий токен равен ":=", "if", "for", "while", "begin", "writeln", "readln", то переходим в operator (оператор)
# Запускаем цикл while, пока лексема будет равна ":" или "/n" (в цикле проверяем два предыдущих условия)
# operator:
# Если текущий токен равен идентификатор, то переходим в assignments (присвоения)
# Если текущий токен равен begin, то переходим в composite (составной)
# Если текущий токен равен if, то переходим в conditional (условный)
# Если текущий токен равен for, то переходим в  fixed_cycle (фиксированный цикл)
# Если текущий токен равен while, то переходим в condition_cycle (условный цикл)
# Если текущий токен равен writeln, то переходим в entry (ввода)
# Если текущий токен равен readln, то переходим в conclusion (вывода)
# composite:
# Если текущий токен равен ":=", "if", "for", "while", "begin", "writeln", "readln", то переходим в operator
# Запуск цикла while, пока лексема будет равна ";" (в цикле проверяем предыдущее условие)
# В конце проверяем, что лексема является "end"
# assignments
# Если лексема равна ":=", то переходим в expression (выражение)
# expression
# Переходим в operand (операнд)
# Запускаем цикл, пока в лексеме встречаются "!=", "==", "<", "<=", ">", ">="
# Повторяем предыдущий шаг, перед циклом
# operand
# Переходим в summand (слагаемое)
# Запускаем цикл, пока в лексеме встречаются "+", "-", "||"
# Повторяем предыдущий шаг, перед циклом
# summand
# Переходим в multiplier (множитель)
# Запускаем цикл, пока в лексеме встречаются "*", "/", "&&"
# Повторяем предыдущий шаг, перед циклом
# multiplier
# Если лексема равна идентификатора, условие выполнено успешно
# Если лексема равна число, то условие выполнено успешно
# Если лексема равно true или false, то переход выполнен успешно
# Если лексема равна "!" (унарная операция), то переходим в multiplier (выражение)
# Если лексема равна "(", то переходим в expression, после выхода проверяем, что следующая лексема равна - ")"
# conditional
# Если лексема равна "(", то переходим в expression (выражение), после выхода проверяем,
# что следующая лексема равна - ")" и после этого переходим в operand (операнд)
# После возвращения из operand (операнд), запускаем цикл while и проверяем есть ли лексема "else"
# В цикле while переходим в operand (операнд)
# fixed_cycle
# Если лексема равна идентификатору, то переходим в assignments (присвоения)
# После этого проверяем, что выбранная лексема равна to
# После этого переходим в expression (выражение)
# После возвращения из expression, запускаем цикл while и проверяем есть ли лексема "step"
# В цикле while пока выполняется условие, переходим в expression
# После цикла переходим в operator (оператор)
# В конце проверяем, что лексема равна "next"
# condition_cycle
# Если лексема, равна "(", то переходим в expression (выражение), после этого проверяем, что лексема равна ")"
# Далее переходим в operator (оператор)
# entry
# Если лексема равна идентификатору, условие выполнено
# Запускаем цикл while и проверяем на наличие в лексеме ","
# Во время работы цикла, проверяем начальное условие на идентификатор


class SyntaxAnalyzer:
    def __init__(self, controller_tokens: ControllerTokens) -> None:
        self.__ct: ControllerTokens = controller_tokens

    def run(self) -> None:
        try:
            p = Program(self.__ct)
            p.action()
        except SyntaxErrors as e:
            print(e)