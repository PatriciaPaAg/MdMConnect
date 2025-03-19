from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Salt(Base):
    __tablename__ = 'salts'
    
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    type = Column(String(50))  # Gusano, chapulín, etc.
    size = Column(Integer)  # Tamaño
    units = Column(String(50))  # Unidades (gr, oz, etc.)

    # Relación con productos
    product = relationship('Product', back_populates='salt')
