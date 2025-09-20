from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)


class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, default="Héroe sin nombre")
    level = Column(Integer, default=1)
    exp = Column(Integer, default=0)
    stats = Column(JSON, default={
        "hp": 100,
        "atk": 10,
        "def": 5,
        "agi": 5
    })
