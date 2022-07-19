from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    username: str


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = "https://github.com/ObelusFamily/Anythink-Market-dre6l/blob/e2f6dafe58284737d47a9fe4fade0ae90f78f539/frontend/public/placeholder.png"


class UserWithToken(User):
    token: str


class UserInResponse(RWSchema):
    user: UserWithToken
