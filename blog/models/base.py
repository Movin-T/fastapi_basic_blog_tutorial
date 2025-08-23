from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class TimestampMixin(SQLModel):
    """Mixin for created_at and updated_at fields."""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)


class BaseModel(SQLModel):
    """Base model with common fields and functionality."""
    pass
