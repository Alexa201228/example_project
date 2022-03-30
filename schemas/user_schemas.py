from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    user_id: int


class UserIn(BaseModel):
    email: EmailStr
    first_name: str


class UserUpdate(UserSchema):
    first_name: str
    last_name: str


class UserOut(UserSchema):
    email = EmailStr

    class Config:
        orm_mode = True
