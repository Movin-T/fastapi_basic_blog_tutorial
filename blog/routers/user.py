from fastapi import APIRouter

from ..database import SessionDep
from ..models import UserCreate, UserPublic
from ..services import UserService

router = APIRouter(prefix='/user', tags=["Users"])

@router.post('/', response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
  return UserService.create_user(session, user)

@router.get('/{user_id}', response_model=UserPublic)
def read_user(user_id: int, session: SessionDep):
  return UserService.get_user_by_id(session, user_id)