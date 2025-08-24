from sqlmodel import Field, Relationship

from blog.models.base import BaseModel
from blog.models.user import User, UserBase


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_id: int | None = Field(default=None, foreign_key="user.id")

    author: User | None = Relationship(back_populates="blogs")


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    title: str | None = None
    body: str | None = None


class BlogPublic(BlogBase):
    id: int
    author: UserBase | None = None
