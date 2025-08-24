from typing import Annotated
from fastapi import APIRouter, Depends

from blog.database import SessionDep
from blog.models import UserCreate, UserPublic, User
from blog.services import UserService
from blog.oauth2 import get_current_user

router = APIRouter(prefix='/user', tags=["Users"])

@router.post('/', response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
  return UserService.create_user(session, user)

@router.get('/me', response_model=UserPublic)
def read_user(current_user: Annotated[User, Depends(get_current_user)]):
  return current_user