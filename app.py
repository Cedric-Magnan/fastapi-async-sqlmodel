import os
from typing import Optional
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


sqlite_file_name = os.environ["SQLITE_FILE_DB_PATH"]
sqlite_url = f"sqlite+aiosqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_async_engine(sqlite_url, future=True, echo=True, connect_args=connect_args)


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


app = FastAPI()


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


@app.post("/heroes/")
async def create_hero(hero: Hero):
    async with AsyncSession(engine) as session:
        session.add(hero)
        await session.commit()
        await session.refresh(hero)
        return hero


@app.get("/heroes/")
async def read_heroes():
    async with AsyncSession(engine) as session:
        heroes = await session.exec(select(Hero))
        return heroes.all()
