# backend/app/schemas/auth_schema.py
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class Token(BaseModel):
    access_token: str
    refresh_token: Optional[str]
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    exp: Optional[int] = None
