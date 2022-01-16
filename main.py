from config import CODE_FILE, TOKEN_FILE
from program import Program


def main() -> None:
    clean_tokens()
    run_program()


def clean_tokens() -> None:
    with open(TOKEN_FILE, 'w', encoding="UTF-8") as file:
        file.write('')


def run_program() -> None:
    with open(CODE_FILE, 'r', encoding="UTF-8") as file:
        read = file.read()
        p = Program(read)
        p.run()


if __name__ == '__main__':
    main()
