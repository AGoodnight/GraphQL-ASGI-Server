from ariadne import ObjectType
from models import ItemsResultBase
from dal import ItemDAL


class ItemQueries():
    def __init__(self, async_session):

        self.items = ObjectType("Query")

        @self.items.field("listItems")
        async def resolve_listItems(*_) -> ItemsResultBase:
            async with async_session() as session:
                async with session.begin():
                    items = ItemDAL(session)
                    return ItemsResultBase(success=True, errors=[""], data=await items.getAllItems())

        @self.items.field("getItem")
        async def resolve_getItem(*_, id):
            async with async_session() as session:
                async with session.begin():
                    items = ItemDAL(session)
                    return ItemsResultBase(success=True, errors=[""], data=await items.getItemById(id))

        @self.items.field("getItemsCreatedAfterDate")
        async def resolve_getItemsCreatedAfterDate(*_, created_at):
            async with async_session() as session:
                async with session.begin():
                    items = ItemDAL(session)
                    return ItemsResultBase(success=True, errors=[""], data=await items.getItemsCreatedAfterDate(created_at))
