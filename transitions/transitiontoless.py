from myutils import reading_next_character_and_cleaning_buffer
from conditions.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class TransitionToLess(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        if self._reader.selected_symbol != '<':
            return False
        reading_next_character_and_cleaning_buffer(self._buffer, self._reader)
        return TypesCondition.M1
