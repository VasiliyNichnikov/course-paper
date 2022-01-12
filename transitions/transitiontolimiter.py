from states.typesstate import TypesState
from transitions.transitionparent import TransitionParent


class TransitionToLimiter(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesState | bool:
        return TypesState.OG
