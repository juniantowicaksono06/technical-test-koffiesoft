from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.sql import func
from models.model import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(String(100), primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
