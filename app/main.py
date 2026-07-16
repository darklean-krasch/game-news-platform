from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base

from app.models.news import News


app = FastAPI(
    title="Game News Platform"
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )


@app.get("/")
async def root():

    return {
        "status": "ok",
        "database": "connected"
    }