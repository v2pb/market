"""
Database connection test script
"""
import asyncio
from app.db.utils import test_connection

async def main():
    """Run database connection test"""
    print("Testing database connection...")
    await test_connection()

if __name__ == "__main__":
    asyncio.run(main())
