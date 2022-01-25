from config import CODE_FILE, TOKEN_FILE
from lexicalanalyzer import LexicalAnalyzer
from syntaxanalyzer import SyntaxAnalyzer
from tokens.tablesoftokens import TablesOfTokens
from tokens.controllertokens import ControllerTokens


def main() -> None:
    clean_tokens()
    run_program()


def clean_tokens() -> None:
    with open(TOKEN_FILE, 'w', encoding="UTF-8") as file:
        file.write('')


def run_program() -> None:
    tables = TablesOfTokens()
    lexical(tables)
    syntax(tables)


def lexical(tables: TablesOfTokens) -> None:
    with open(CODE_FILE, 'r', encoding="UTF-8") as file:
        code = file.read()
        la = LexicalAnalyzer(tables, code)
        la.run()


def syntax(tables: TablesOfTokens) -> None:
    controller_tokens = ControllerTokens(tables)
    sa = SyntaxAnalyzer(controller_tokens)
    sa.run()

if __name__ == '__main__':
    main()
