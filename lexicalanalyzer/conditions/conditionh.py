from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.checkingsymbol import CheckingSymbol
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from myutils import cleaning_buffer_reading_next_character
from tokens.workingwithtoken import WorkingWithToken


class ConditionH(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition):
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self.__cleaning_from_code()
        checking_symbol = CheckingSymbol()
        if checking_symbol.is_value_letter(self._reader.selected_symbol):
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.I
        elif self._reader.selected_symbol in ['0', '1']:
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N2
        elif self._reader.selected_symbol in ['2', '3', '4', '5', '6', '7']:
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N8
        elif self._reader.selected_symbol in ['8', '9']:
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.N10
        elif self._reader.selected_symbol == '.':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.P1
        elif self._reader.selected_symbol == '(':
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.C1
        elif self._reader.selected_symbol == '<':
            # cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.M1
        elif self._reader.selected_symbol == '>':
            # cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.M2
        elif self._reader.selected_symbol == ':':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.ASSIGNMENT
        elif self._reader.selected_symbol == '=':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.EQUALLY
        elif self._reader.selected_symbol == '!':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.UNEQUAL
        elif self._reader.selected_symbol == '|':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.OR
        elif self._reader.selected_symbol == '&':
            cleaning_buffer_reading_next_character(self._buffer, self._reader)
            self._condition.now = TypesCondition.AND
        else:
            self._condition.now = TypesCondition.OG

    def __cleaning_from_code(self) -> None:
        while self._reader.selected_symbol in [' ']:
            self._reader.trip_first_character()
