from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "to-do list API"}

class Item(BaseModel):
    id: int | None = None
    text: str
    is_done: bool = False

class ItemUpdate(BaseModel):
    text: str | None = None
    is_done: bool | None = None

items = []
counter = 0

@app.post("/items", response_model=Item)
def create_item(item: Item):
    global counter
    counter += 1
    item.id = counter
    items.append(item)
    return item

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"item {item_id} not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail=f"item {item_id} not found")

@app.patch("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: ItemUpdate):
    if item_id <= 0:
        raise HTTPException(400, "invalid id")
    
    for item in items:
        
        if item.id == item_id:

            if updated.text is not None:
                item.text = updated.text

            if updated.is_done is not None:
                item.is_done = updated.is_done

            return item
        
    raise HTTPException(status_code=404, detail="item not found")