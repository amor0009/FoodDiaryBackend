from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Double
from sqlalchemy.orm import relationship
from src.database.database import Base
from src.models.user_weight import UserWeight


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    weight = Column(Double, nullable=True)
    gender = Column(String, nullable=True)
    aim = Column(String, nullable=True)
    recommended_calories = Column(Double, nullable=True)
    profile_image = Column(String, nullable=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow())

    meals = relationship('Meal', back_populates='user')
    products = relationship("Product", back_populates="user")
    recorded_weight = relationship("UserWeight", back_populates="user")