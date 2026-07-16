from fastapi import FastAPI

app = FastAPI(
    title="Game News Platform"
)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "game-news-platform"
    }