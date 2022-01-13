from conditions.typescondition import TypesCondition
from transitions.transitionparent import TransitionParent


class TransitionToLimiter(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        return TypesCondition.OG
