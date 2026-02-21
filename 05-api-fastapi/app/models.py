from sqlalchemy import Column, Integer
from app.database import Base

class Number(Base):
    __tablename__ = "numbers"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False)
