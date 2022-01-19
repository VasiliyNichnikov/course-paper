from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from myutils import reading_next_character
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken


class ConditionOr(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '|':
            reading_next_character(self._buffer, self._reader)
            self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
        self._condition.now = TypesCondition.H
