"""
Models package for the blog application.

This package contains all database models and Pydantic schemas
organized by domain (user, blog) for better maintainability.
"""

# Import all models for convenience
from .user import User, UserBase, UserCreate, UserUpdate, UserPublic
from .blog import Blog, BlogBase, BlogCreate, BlogUpdate, BlogPublic
from .base import BaseModel, TimestampMixin

__all__ = [
    # User models
    "User", "UserBase", "UserCreate", "UserUpdate", "UserPublic",
    # Blog models  
    "Blog", "BlogBase", "BlogCreate", "BlogUpdate", "BlogPublic",
    # Base models
    "BaseModel", "TimestampMixin"
]
