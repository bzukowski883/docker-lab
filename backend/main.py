import asyncpg
from fastapi import FastAPI

app = FastAPI()

async def get_db():
    return await asyncpg.connect(
        user="postgres",
        password="postgres",
        database="sampledb",
        host="postgres"  # service name in docker-compose
    )

@app.get("/users")
async def get_users():
    conn = await get_db()
    rows = await conn.fetch("SELECT id, name, email FROM users;")
    await conn.close()
    return [dict(r) for r in rows]
