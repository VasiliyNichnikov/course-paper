from myutils import reading_next_character_and_cleaning_buffer
from states.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class TransitionToClosingCurlyBrace(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        if self._reader.selected_symbol != '}':
            return False
        self._token.writing_to_token_file(2, 2)
        reading_next_character_and_cleaning_buffer(self._buffer, self._reader)
        return TypesCondition.V
