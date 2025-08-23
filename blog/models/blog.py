from sqlmodel import Field, Relationship
from .base import BaseModel
from .user import User, UserBase


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_id: int | None = Field(default=None, foreign_key="user.id")

    author: User | None = Relationship(back_populates="blogs")


class BlogCreate(BlogBase):
    author_id: int


class BlogUpdate(BlogBase):
    title: str | None = None
    body: str | None = None


class BlogPublic(BlogBase):
    id: int
    author: UserBase | None = None
