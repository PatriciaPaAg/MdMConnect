from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Craft(Base):
    __tablename__ = 'crafts'
    
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    c_type = Column(String(50))  # Ej. caballito, cuchara, botella pintada, etc.
    material = Column(String(50))  # Madera, barro, etc.
    size = Column(String(50))  # Chico, mediano, etc.

    # Relación con productos
    product = relationship('Product', back_populates='craft')
