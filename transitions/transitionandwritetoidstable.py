from conditions.typescondition import TypesCondition
from tokens.typesoftokentables import TypesOfTokenTables
from transitions.transitionparent import TransitionParent


class TransitionAndWriteToIdsTable(TransitionParent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def action(self) -> TypesCondition | bool:
        self._token.writing_token_to_table(TypesOfTokenTables.IDS)
        self._token.writing_to_token_file(3, self._token.z)
        return TypesCondition.H
