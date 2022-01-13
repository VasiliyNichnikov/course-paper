from myutils import reading_next_character_and_cleaning_buffer
from states.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class TransitionToOctalNotation(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        if self._reader.selected_symbol not in ['2', '3', '4', '5', '6', '7']:
            return False
        reading_next_character_and_cleaning_buffer(self._buffer, self._reader)
        return TypesCondition.N8
