from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from blog.jwtToken import verify_access_token
from blog.database import SessionDep
from blog.services import UserService
from blog.models import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: SessionDep
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    
    user = UserService.get_user_for_auth(session, int(token_data.user_id))
    
    return user

CurrentUserDep = Annotated[User, Depends(get_current_user)]