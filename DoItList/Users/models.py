from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from DoItList.database import Base
from DoItList.Items.models import Items

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    items = relationship('Items', back_populates='user')
