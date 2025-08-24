from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING

from blog.models.base import BaseModel

# Avoid circular imports
if TYPE_CHECKING:
    from blog.models import Blog


class UserBase(BaseModel):
    name: str
    email: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str = Field(..., min_length=8)

    blogs: list["Blog"] = Relationship(back_populates="author")


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None


class UserPublic(UserBase):
    id: int
    # Note: blogs relationship will be populated by the relationship, 
    # but we avoid importing Blog here to prevent circular imports
