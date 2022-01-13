from conditions.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class TransitionAndWritingToServiceTable(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        if self._token.z == 0:
            return False
        self._token.writing_to_token_file(0, self._token.z)
        return TypesCondition.H
