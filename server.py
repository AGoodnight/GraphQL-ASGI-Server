
from datetime import datetime
from ariadne import ScalarType
import uvicorn
from yaml import safe_load

from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

import scalars
from queries import ItemQueries
from mutations import ItemMutations


def loadConfig():
    return safe_load(Path('app.config.yaml').read_text())


config = loadConfig()

type_defs = load_schema_from_path('graphql/schema.graphql')

engine = create_async_engine(
    config['SQLALCHEMY_DATABASE_URI'], future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

queries = ItemQueries(async_session)
mutations = ItemMutations(async_session)

schema = make_executable_schema(
    type_defs, queries.items, mutations.items, scalars.datetime_scalar)

app = GraphQL(schema)


if __name__ == "__main__":
    uvicorn.run("__main__:app",
                host=config['HOST'], port=config['PORT'], reload=True)
