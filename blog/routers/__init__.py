"""
Routers module for API endpoints.

This module contains all FastAPI routers that define the API endpoints
and handle HTTP requests/responses.
"""

from .blog import router as blog_router
from .user import router as user_router

__all__ = ["blog_router", "user_router"]