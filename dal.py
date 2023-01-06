
import uuid as uuid_pkg
import sqlalchemy as sa
from sqlalchemy_utils.functions import cast_if
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import table, update
from datetime import datetime

from models import Item


class ItemDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def getAllItems(self) -> list[Item]:
        result = await self.db_session.execute(select(Item).order_by(Item.id))
        return result.scalars().all()

    async def getItemById(self, id: str) -> Item:
        result = await self.db_session.execute(select(Item).where(Item.id == id))
        return result.scalars().all()

    async def getItemsByCategory(self, category: str) -> list[Item]:
        result = await self.db_session.execute(select(Item).where(cast_if(Item.category, sa.String) == category))
        return result.scalars().all()

    async def getItemsCreatedAfterDate(self, date: str) -> list[Item]:
        result = await self.db_session.execute(select(Item).where(Item.created_at >= datetime.fromisoformat(date)))
        return result.scalars().all()

    async def updateItemDescription(self, id: str, description: str) -> list[str]:
        print("---------> REPLACE:", description, id)
        result = await self.db_session.execute(update(Item).where(Item.description == id).returning(Item.id).values(description=description))
        print("----------->RETURNING:", result.scalars().all())
        return result.scalars().all()
