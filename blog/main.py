from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, status
from sqlmodel import select

from blog.database import SessionDep, create_db_and_tables
from blog.models import Blog, BlogCreate, BlogPublic, BlogUpdate, User, UserBase, UserCreate, UserPublic
from blog.hashing import Hash

app = FastAPI()

@app.on_event("startup")
def on_startup():
  create_db_and_tables()

@app.post('/blog', response_model=BlogPublic, tags=["Blogs"])
def create_blog(request: BlogCreate, session: SessionDep):
  db_blog = Blog.model_validate(request)
  session.add(db_blog)
  session.commit()
  session.refresh(db_blog)
  return db_blog

@app.get('/blog', response_model=list[BlogPublic], tags=["Blogs"])
def read_blogs(
  session: SessionDep, 
  offset: Annotated[int, Query(ge=0)] = 0,
  limit: Annotated[int, Query(le=100)] = 100,
):
  blogs = session.exec(
    select(Blog).offset(offset).limit(limit)
  ).all()
  return blogs

@app.get('/blog/{blog_id}', response_model=BlogPublic, tags=["Blogs"])
def read_blog(blog_id: int, session: SessionDep):
  blog = session.get(Blog, blog_id)
  if not blog:
    raise HTTPException(status_code=404, detail="Blog not found")
  return blog

@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def delete_blog(blog_id: int, session: SessionDep):
  blog = session.get(Blog, blog_id)
  if not blog:
    raise HTTPException(status_code=404, detail="Blog not found")
  session.delete(blog)
  session.commit()
  return None

@app.patch('/blog/{blog_id}', response_model=BlogPublic, tags=["Blogs"])
def update_blog(blog_id: int, request: BlogUpdate, session: SessionDep):
  blog_db = session.get(Blog, blog_id)
  if not blog_db:
    raise HTTPException(status_code=404, detail="Blog not found")
  blog_data = request.model_dump(exclude_unset=True)
  blog_db.sqlmodel_update(blog_data)
  session.add(blog_db)
  session.commit()
  session.refresh(blog_db)
  return blog_db

@app.post('/user', response_model=UserPublic, tags=["Users"])
def create_user(user: UserCreate, session: SessionDep):
  db_user = User(name=user.name, email=user.email, password=Hash.bcrypt(user.password))
  session.add(db_user)
  session.commit()
  session.refresh(db_user)
  return db_user

@app.get('/user/{user_id}', response_model=UserPublic, tags=["Users"])
def read_user(user_id: int, session: SessionDep):
  user = session.get(User, user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user