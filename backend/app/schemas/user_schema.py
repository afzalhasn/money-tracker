# backend/app/schemas/user_schema.py
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
import enum

class Role(str, enum.Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"

class UserCreate(BaseModel):
    username: str
    password: str
    full_name: Optional[str]
    role: Role = Role.STAFF

class UserRead(BaseModel):
    id: UUID
    username: str
    full_name: Optional[str]
    role: Role
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
