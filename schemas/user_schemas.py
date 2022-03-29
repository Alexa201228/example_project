from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    email: EmailStr


class UserOut(UserSchema):
    email = EmailStr

    class Config:
        orm_mode = True


class UserUpdate(UserSchema):
    first_name: str
    last_name: str