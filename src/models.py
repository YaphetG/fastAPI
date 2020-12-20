from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


class User(BaseModel):
    id: str
    name: str
    email: Optional[str] = None


class Post(BaseModel):
    id: str
    ownedBy: User
    items: List[Item] = []

