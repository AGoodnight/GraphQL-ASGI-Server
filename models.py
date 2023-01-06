from sqlmodel import Field, SQLModel, text
import uuid as uuid_pkg
from datetime import datetime


class ItemBase(SQLModel):
    category: str
    description: str


class ItemsResultBase(SQLModel):
    success: bool
    errors: list[str]
    data: list[ItemBase]


class ItemsMutationResultBase(SQLModel):
    success: bool
    errors: list[str]
    data: list[str]


class UUIDModel(SQLModel):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("gen_random_uuid()"),
            "unique": True
        }
    )


class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)")
        }
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)")
        }
    )


class Item(TimestampModel, ItemBase, UUIDModel, table=True):
    __tablename__ = f'items'
