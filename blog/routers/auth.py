from fastapi import APIRouter
from sqlmodel import select

from ..database import SessionDep
from ..models import Login, Token
from ..services import AuthService

router = APIRouter(prefix='/auth', tags=["Authentication"])

@router.post('/login', response_model=Token)
def login(request: Login, session: SessionDep):
    return AuthService.authenticate_user(session, request.email, request.password)