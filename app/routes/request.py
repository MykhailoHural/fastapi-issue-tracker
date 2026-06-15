from fastapi import APIRouter
from app.db.items import items

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/items")
def get_items():
    return items


@router.get("/items/{item_id}")
async def get_items_by_id(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@router.post("/items")
async def post_new_item(item: dict):
    items.append(item)
    return items
