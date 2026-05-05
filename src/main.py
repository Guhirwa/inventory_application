"""Entry point of the system"""
from typing import Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from .utils import find_item

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
    
@fastapi.exception_handler(Exception)
async  def global_exception_handler(request: Request, exc: Exception):
    """global exception handler"""
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again."}
    )

@fastapi.get('/home/{username}')
async def home(username: str):
    """Home route handler to welcome the user wih a greet message"""
    return {'message': f'Hello {username}, Welcome !!!'}

@fastapi.get('/items')
async def get_items():
    """Route handler for get all items"""
    return {'items': inventory}

@fastapi.get('/items/{item_id}')
async def get_item(item_id: int):
    """Route handler for calling the searching functionality"""
    if item_id <= 0:
        raise HTTPException(
            status_code=404,
            detail='Invalid ID. ID must be greater that 0'
        )
    item, idx = find_item(inventory, lambda x: x['id'] == item_id)
    return {'item': item}

@fastapi.delete('/items/{item_id}')
async def delete_item(item_id: int):
    """Route handler for the delete functionality"""
    item, idx = find_item(inventory, lambda x: x['id'] == item_id)
    if idx == -1:
        return HTTPException(404, 'item not found')
    inventory.pop(idx)
    return {'item': item}

@fastapi.post('/items')
async def add_item(data: Item):
    """Route handler for add a new item in the database"""
    item = {
        'id': len(inventory) + 1,
        'name': data.name,
        'quantity': data.quantity
    }
    inventory.append(item)
    return item

@fastapi.patch('/items/{item_id}')
async def update_item(item_id: int, item_update: ItemUpdate):
    """Router Handler for updating the already saved item"""
    item, idx = find_item(inventory, lambda x: x['id'] == item_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail='item not found')
    if item_update.name is not None:
        item['name'] = item_update.name
    if item_update.quantity is not None:
        item['quantity'] = item_update.quantity
    inventory[idx] = item
    return item
