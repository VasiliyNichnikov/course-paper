from buffer import Buffer
from characterreader import CharacterReader
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken
from workingwithnumber import WorkingWithNumber


def cleaning_buffer_reading_next_character(buffer: Buffer, reader: CharacterReader) -> None:
    buffer.clear()
    buffer.add(reader.selected_symbol)
    reader.trip_first_character()


def reading_next_character(buffer: Buffer, reader: CharacterReader) -> None:
    buffer.add(reader.selected_symbol)
    reader.trip_first_character()


def converting_numbers_writing_to_tokens(buffer: Buffer, token: WorkingWithToken, base: int) -> None:
    actions_numbers = WorkingWithNumber()
    number: str = buffer.get_combined_characters()
    new_number = actions_numbers.conversion_from_number_system_to_decimal(number, base)
    buffer.clear()
    buffer.add(new_number)
    token.writing_token_to_table(TypesOfTokenTables.NUMBERS)
    token.writing_token_to_file(3, token.z)


def converting_string_to_numbers_writing_to_tokens(buffer: Buffer, token: WorkingWithToken) -> None:
    actions_numbers = WorkingWithNumber()
    number: str = buffer.get_combined_characters()
    new_number = actions_numbers.converting_from_string_to_decimal_form(number)
    buffer.clear()
    buffer.add(new_number)
    token.writing_token_to_table(TypesOfTokenTables.NUMBERS)
    token.writing_token_to_file(2, token.z)
