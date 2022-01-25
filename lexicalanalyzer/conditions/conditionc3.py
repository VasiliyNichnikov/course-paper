from lexicalanalyzer.buffer import Buffer
from lexicalanalyzer.characterreader import CharacterReader
from lexicalanalyzer.conditions.condition import Condition
from lexicalanalyzer.conditions.conditionparent import ConditionParent
from lexicalanalyzer.conditions.typescondition import TypesCondition
from tokens.workingwithtoken import WorkingWithToken


class ConditionC3(ConditionParent):
    def __init__(self, reader: CharacterReader, buffer: Buffer, token: WorkingWithToken, condition: Condition) -> None:
        super().__init__(reader, buffer, token, condition)

    def action(self) -> None:
        if self._reader.selected_symbol == ')':
            self._reader.trip_first_character()
            self._condition.now = TypesCondition.H
        else:
            self._condition.now = TypesCondition.C2
