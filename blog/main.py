from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, status
from sqlmodel import select

from blog.database import SessionDep, create_db_and_tables
from blog.models import Blog, BlogCreate

app = FastAPI()

@app.on_event("startup")
def on_startup():
  create_db_and_tables()

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: BlogCreate, session: SessionDep) -> Blog:
  db_blog = Blog.model_validate(request)
  session.add(db_blog)
  session.commit()
  session.refresh(db_blog)
  return db_blog

@app.get('/blog')
def read_blogs(
  session: SessionDep, 
  offset: Annotated[int, Query(ge=0)] = 0,
  limit: Annotated[int, Query(le=100)] = 100,
) -> list[Blog]:
  blogs = session.exec(
    select(Blog).offset(offset).limit(limit)
  ).all()
  return blogs

@app.get('/blog/{blog_id}')
def read_blog(blog_id: int, session: SessionDep) -> Blog:
  blog = session.get(Blog, blog_id)
  if not blog:
    raise HTTPException(status_code=404, detail="Blog not found")
  return blog

@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, session: SessionDep):
  blog = session.get(Blog, blog_id)
  if not blog:
    raise HTTPException(status_code=404, detail="Blog not found")
  session.delete(blog)
  session.commit()
  return None

@app.put('/blog/{blog_id}', status_code=status.HTTP_200_OK)
def update_blog(blog_id: int, request: BlogCreate, session: SessionDep) -> Blog:
  blog = session.get(Blog, blog_id)
  if not blog:
    raise HTTPException(status_code=404, detail="Blog not found")
  
  updated_blog = Blog.model_validate(request)
  blog.title = updated_blog.title
  blog.body = updated_blog.body
  session.add(blog)
  session.commit()
  session.refresh(blog)
  
  return blog