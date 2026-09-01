from pydantic import BaseModel

class Expense(BaseModel):
    id: int | None = None
    category: str
    amount: float

