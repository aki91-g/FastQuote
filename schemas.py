from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    is_active: bool = True
    full_name: Optional[str] = None
    class Config:
        orm_mode = True

class QuoteBase(BaseModel):
    text: str


class QuoteRead(QuoteBase):
    id: int
    author_id: Optional[int] = None
    class Config:
        orm_mode = True

