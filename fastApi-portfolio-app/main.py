from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from routers import user
from db.session import engine
from models.user import Base


app = FastAPI()

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

app.include_router(user.router)