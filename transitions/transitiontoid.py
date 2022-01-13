from myutils import reading_next_character_and_cleaning_buffer
from conditions.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class TransitionToId(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        if not self._checking_symbol.is_value_letter(self._reader.selected_symbol):
            return False
        reading_next_character_and_cleaning_buffer(self._buffer, self._reader)
        return TypesCondition.I
