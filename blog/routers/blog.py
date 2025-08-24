from fastapi import APIRouter, Query, status
from typing import Annotated

from blog.models import BlogPublic, BlogCreate, BlogUpdate, User
from blog.database import SessionDep
from blog.services import BlogService
from blog.oauth2 import CurrentUserDep

router = APIRouter(prefix='/blog' ,tags=["Blogs"])

@router.post('/', response_model=BlogPublic)
def create_blog(request: BlogCreate, session: SessionDep, current_user: CurrentUserDep):
  return BlogService.create_blog(session, request, current_user.id)

@router.get('/', response_model=list[BlogPublic], )
def read_blogs(
  session: SessionDep,
  offset: Annotated[int, Query(ge=0)] = 0,
  limit: Annotated[int, Query(le=100)] = 100,
):
  return BlogService.get_blogs(session, offset, limit)

@router.get('/{blog_id}', response_model=BlogPublic)
def read_blog(blog_id: int, session: SessionDep):
  return BlogService.get_blog_by_id(session, blog_id)

@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, session: SessionDep, current_user: CurrentUserDep):
  BlogService.delete_blog(session, blog_id, current_user.id)
  return None

@router.patch('/{blog_id}', response_model=BlogPublic)
def update_blog(blog_id: int, request: BlogUpdate, session: SessionDep, current_user: CurrentUserDep):
  return BlogService.update_blog(session, blog_id, request, current_user.id)
