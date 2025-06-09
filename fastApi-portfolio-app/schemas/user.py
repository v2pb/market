from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    is_active: bool = False  # Changed from str to bool with default False


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }