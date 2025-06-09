"""
Database connection testing utility
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from .session import engine

async def test_connection():
    """Test the database connection."""
    try:
        async with engine.connect() as conn:
            # Try a simple query
            result = await conn.execute(text("SELECT 1"))
            await conn.commit()
            
            if result:
                print("✅ Successfully connected to PostgreSQL database!")
                return True
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    asyncio.run(test_connection())
