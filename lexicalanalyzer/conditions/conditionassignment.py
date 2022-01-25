from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken
from myutils import reading_next_character


class ConditionAssignment(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '=':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H

