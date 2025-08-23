from typing import List
from fastapi import HTTPException, status
from sqlmodel import Session, select

from ..models import Blog, BlogCreate, BlogUpdate, BlogPublic


class BlogService:
    """Service class for blog-related business logic."""
    
    @staticmethod
    def create_blog(session: Session, blog_data: BlogCreate) -> Blog:
        """Create a new blog post."""
        db_blog = Blog.model_validate(blog_data)
        session.add(db_blog)
        session.commit()
        session.refresh(db_blog)
        return db_blog
    
    @staticmethod
    def get_blogs(session: Session, offset: int = 0, limit: int = 100) -> List[BlogPublic]:
        """Retrieve a list of blog posts with pagination."""
        blogs = session.exec(
            select(Blog).offset(offset).limit(limit)
        ).all()
        return blogs
    
    @staticmethod
    def get_blog_by_id(session: Session, blog_id: int) -> BlogPublic:
        """Retrieve a single blog post by ID."""
        blog = session.get(Blog, blog_id)
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Blog not found"
            )
        return blog
    
    @staticmethod
    def update_blog(session: Session, blog_id: int, blog_update: BlogUpdate) -> Blog:
        """Update an existing blog post."""
        blog_db = session.get(Blog, blog_id)
        if not blog_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Blog not found"
            )
        
        blog_data = blog_update.model_dump(exclude_unset=True)
        blog_db.sqlmodel_update(blog_data)
        session.add(blog_db)
        session.commit()
        session.refresh(blog_db)
        return blog_db
    
    @staticmethod
    def delete_blog(session: Session, blog_id: int) -> None:
        """Delete a blog post by ID."""
        blog = session.get(Blog, blog_id)
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Blog not found"
            )
        
        session.delete(blog)
        session.commit()
