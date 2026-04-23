from pydoc import describe
from unittest.mock import Base

from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from sqlalchemy import desc

fastapi = FastAPI()


class Item(BaseModel):
    """Pydantic model for item structure and validation"""

    name: str
    quantity: int


class ItemUpdate(BaseModel):
    """Pydantic model from updated item structure and validation"""

    name: Optional[str] = Field(None, description="Optional name for an Item")
    quantity: Optional[int] = Field(None, description="Optional quantity of an Item")
