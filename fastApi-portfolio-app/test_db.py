import asyncio
from core.config import settings
import asyncpg

async def test_database_connection():
    try:
        # Create a connection
        conn = await asyncpg.connect(
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB
        )
        
        # Test the connection with a simple query
        version = await conn.fetchval('SELECT version();')
        print("Successfully connected to the database!")
        print(f"PostgreSQL version: {version}")
        
        # Close the connection
        await conn.close()
        
    except Exception as e:
        print("Failed to connect to the database!")
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_database_connection())
