from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from blog.database import SessionDep
from blog.models import Token
from blog.services import AuthService

router = APIRouter(prefix='/auth', tags=["Authentication"])

@router.post('/login', response_model=Token)
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep):
    return AuthService.authenticate_user(session, request.username, request.password)