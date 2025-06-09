from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User
from schemas.user import UserCreate, UserOut
from core.hashing import get_password_hash
from db.session import get_db
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/",response_model=List[UserOut])
async def get_users( db: AsyncSession = Depends(get_db)):
    query  = select(User)
    result  = await db.execute(query)
    users = result.scalars().all()
    return users


@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if user exists
    query = select(User).where(User.email == user.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Create new user
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        is_active=True 
    )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    
    return db_user
