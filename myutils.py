from buffer import Buffer
from characterreader import CharacterReader


def reading_next_character_and_cleaning_buffer(buffer: Buffer, reader: CharacterReader) -> None:
    buffer.clear()
    buffer.add(reader.selected_symbol)
    reader.trip_first_character()


def reading_next_character(buffer: Buffer, reader: CharacterReader) -> None:
    buffer.add(reader.selected_symbol)
    reader.trip_first_character()
