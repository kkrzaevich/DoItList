from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from DoItList.database import Base


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    descriptions = Column(String)
    user_id = Column(ForeignKey('users.id'))
    user = relationship('Users', back_populates='items')
