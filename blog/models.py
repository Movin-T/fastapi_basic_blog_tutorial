from sqlmodel import Field, Relationship, SQLModel

class UserBase(SQLModel):
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
  blogs: list["Blog"]


class BlogBase(SQLModel):
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
  author: UserPublic | None = None