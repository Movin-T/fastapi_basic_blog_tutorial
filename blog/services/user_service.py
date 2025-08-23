from fastapi import HTTPException, status
from sqlmodel import Session, select

from ..models import User, UserCreate, UserPublic
from ..hashing import Hash


class UserService:
    """Service class for user-related business logic."""
    
    @staticmethod
    def create_user(session: Session, user_data: UserCreate) -> User:
        """Create a new user with business logic validation."""
        # Business logic: Check if email already exists
        existing_user = session.exec(
            select(User).where(User.email == user_data.email)
        ).first()
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Business logic: Hash password before storing
        hashed_password = Hash.bcrypt(user_data.password)
        
        # Create user with hashed password
        db_user = User(
            name=user_data.name, 
            email=user_data.email, 
            password=hashed_password
        )
        
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_id(session: Session, user_id: int) -> User:
        """Retrieve a single user by ID."""
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User not found"
            )
        return user
