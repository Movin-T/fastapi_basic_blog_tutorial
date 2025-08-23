from sqlmodel import Field, SQLModel

class BlogBase(SQLModel):
  title: str
  body: str

class Blog(BlogBase, table=True):
  id: int | None = Field(default=None, primary_key=True)

class BlogCreate(BlogBase):
  pass

class BlogUpdate(BlogBase):
  title: str | None = None
  body: str | None = None

class BlogPublic(BlogBase):
  id: int


class UserBase(SQLModel):
  name: str
  email: str

class User(UserBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  password: str = Field(..., min_length=8)

class UserCreate(UserBase):
  password: str

class UserUpdate(UserBase):
  name: str | None = None
  email: str | None = None
  password: str | None = None

class UserPublic(UserBase):
  id: int