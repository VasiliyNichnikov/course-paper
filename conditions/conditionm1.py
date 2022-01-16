from buffer import Buffer
from characterreader import CharacterReader
from conditions.condition import Condition
from conditions.conditionparent import ConditionParent
from conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken


class ConditionM1(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == '>':
            self._reader.trip_first_character()
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 17)
        elif self._reader.selected_symbol == '=':
            self._reader.trip_first_character()
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 20)
        else:
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, 19)
        self._condition.now = TypesCondition.H
