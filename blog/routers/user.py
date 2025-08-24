from typing import Annotated
from fastapi import APIRouter, Depends

from ..database import SessionDep
from ..models import UserCreate, UserPublic, User
from ..services import UserService
from ..oauth2 import get_current_user

router = APIRouter(prefix='/user', tags=["Users"])

@router.post('/', response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
  return UserService.create_user(session, user)

@router.get('/me', response_model=UserPublic)
def read_user(current_user: Annotated[User, Depends(get_current_user)]):
  return current_user