from fastapi import HTTPException, status
from sqlmodel import Session, select
from datetime import timedelta

from ..models import User, Token
from ..hashing import Hash
from ..jwtToken import create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthService:
  """Service for handling authentication logic."""

  @staticmethod
  def authenticate_user(session: Session, email: str, password: str) -> Token:
    user =  session.exec(select(User).where(User.email == email)).first()
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    if not Hash.verify(user.password, password):
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
