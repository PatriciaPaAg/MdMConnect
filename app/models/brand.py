from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Brand(Base):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    mezcal_house_id = Column(Integer, ForeignKey('mezcal_houses.id', ondelete='CASCADE'))

    # Relaciones
    mezcal_house = relationship('MezcalHouse', back_populates='brands')
    products = relationship('Product', back_populates='brand')
