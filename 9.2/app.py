from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = ""


items = [
    {"id": 1, "name": "Item 1", "description": "Primeiro item"},
    {"id": 2, "name": "Item 2", "description": "Segundo item"},
]
next_id = 3


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    new_item = {"id": next_id, "name": item.name, "description": item.description}
    items.append(new_item)
    next_id += 1
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    existing = next((i for i in items if i["id"] == item_id), None)
    if existing is None:
        raise HTTPException(status_code=404, detail="Item not found")
    existing["name"] = item.name
    existing["description"] = item.description
    return existing


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    existing = next((i for i in items if i["id"] == item_id), None)
    if existing is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items = [i for i in items if i["id"] != item_id]
    return {"message": f"Item {item_id} deleted successfully"}
