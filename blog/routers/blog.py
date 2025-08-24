from fastapi import APIRouter, Depends, Query, status
from typing import Annotated

from ..models import BlogPublic, BlogCreate, BlogUpdate, User
from ..database import SessionDep
from ..services import BlogService
from ..oauth2 import get_current_user

router = APIRouter(prefix='/blog' ,tags=["Blogs"])

@router.post('/', response_model=BlogPublic)
def create_blog(request: BlogCreate, session: SessionDep, current_user: Annotated[User, Depends(get_current_user)]):
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
def delete_blog(blog_id: int, session: SessionDep):
  BlogService.delete_blog(session, blog_id)
  return None

@router.patch('/{blog_id}', response_model=BlogPublic)
def update_blog(blog_id: int, request: BlogUpdate, session: SessionDep):
  return BlogService.update_blog(session, blog_id, request)
