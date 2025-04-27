from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.schemas.product import ProductOut

class OrderCreate(BaseModel):
    customer_id: int
    product_ids: List[int]

class OrderOut(BaseModel):
    id: int
    customer_id: int
    created_at: datetime
    products: List[ProductOut]
    total_cost: float

    class Config:
        orm_mode = True
