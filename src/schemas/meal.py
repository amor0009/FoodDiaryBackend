from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from src.schemas.product import ProductRead
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.schemas.meal_products import MealProductsCreate, MealProductsUpdate


class MealRead(BaseModel):
    id: int
    name: str
    weight: float
    calories: float
    proteins: float
    fats: float
    carbohydrates: float
    recorded_at: datetime
    user_id: int
    products: Optional[List[ProductRead]] = []

    class Config:
        from_attributes = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "calories": self.calories,
            "proteins": self.proteins,
            "fats": self.fats,
            "carbohydrates": self.carbohydrates,
            "recorded_at": self.recorded_at.isoformat(),
            "user_id": self.user_id,
            "products": [product.dict() for product in self.products] if self.products else []
        }

class MealUpdate(BaseModel):
    name: str
    weight: float
    calories: float
    proteins: float
    fats: float
    carbohydrates: float
    products: Optional[List['MealProductsUpdate']] = []


class MealCreate(BaseModel):
    name: str
    weight: float
    calories: float
    proteins: float
    fats: float
    carbohydrates: float
    products: Optional[List['MealProductsCreate']] = []

