
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class MezcalHouse(Base):
    __tablename__ = 'mezcal_houses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    contactPerson = Column(String(50))
    contactNumber = Column(String(10))

    # Relación con brands
    brands = relationship('Brand', back_populates='mezcal_house')
