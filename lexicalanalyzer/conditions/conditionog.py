from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from tokens.workingwithtoken import WorkingWithToken


class ConditionOG(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        self._buffer.clear()
        self._buffer.add(self._reader.selected_symbol)
        self._token.find_token_in_selected_table(TypesOfTokenTables.LIMITERS)

        if self._token.z != -1:
            self._reader.trip_first_character()
            self._token.writing_token_to_file(TypesOfTokenTables.LIMITERS, self._token.z)
            self._condition.now = TypesCondition.H
        else:
            self._condition.now = TypesCondition.ER
