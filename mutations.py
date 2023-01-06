from ariadne import ObjectType
from models import ItemsResultBase, ItemsMutationResultBase
from dal import ItemDAL


class ItemMutations():
    def __init__(self, async_session):

        self.items = ObjectType("Mutation")

        @self.items.field('updateItemDescription')
        async def updateItemDescription(_, info, id: str, description: str) -> ItemsMutationResultBase:
            async with async_session() as session:
                async with session.begin():
                    items = ItemDAL(session)
                    return ItemsMutationResultBase(success=True, errors=[""], data=await items.updateItemDescription(id, description))
