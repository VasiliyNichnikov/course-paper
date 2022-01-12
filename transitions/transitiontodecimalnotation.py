from myutils import reading_next_character_and_cleaning_buffer
from states.typesstate import TypesState
from transitions.transitionparent import TransitionParent


class TransitionToDecimalNotation(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesState | bool:
        if self._reader.selected_symbol not in ['8', '9']:
            return False
        reading_next_character_and_cleaning_buffer(self._buffer, self._reader)
        return TypesState.N10
