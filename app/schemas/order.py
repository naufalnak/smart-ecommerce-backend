from pydantic import BaseModel

class OrderOut(BaseModel):
    id: int
    total_price: float

    class Config:
        from_attributes = True