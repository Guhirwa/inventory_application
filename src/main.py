'''Entry point of the system'''
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from utils import find_item

fastapi = FastAPI()

inventory = [
    {'id': 1, 'name': 'Treasure', 'quantity': 3}
]

class Item(BaseModel):
    """Pydantic model for item structure and validation"""

    name: str
    quantity: int


class ItemUpdate(BaseModel):
    """Pydantic model from updated item structure and validation"""

    name: Optional[str] = Field(None, description="Optional name for an Item")
    quantity: Optional[int] = Field(None, description="Optional quantity of an Item")

@fastapi.get('/{username}')
async def home(username: str):
    '''Home route handler to welcome the user wih a greet message'''
    return {'message': f'Hello {username}, Welcome !!!'}

@fastapi.get('/items')
async def get_items():
    '''Route handler for get all items'''
    return {'items': inventory}

@fastapi.get('/items/{item_id}')
async def get_item(item_id: int):
    '''Route handler for calling the searching functionality'''
    item, idx = find_item(inventory, lambda x: x['id'] == item_id)
    return {'item': item}
