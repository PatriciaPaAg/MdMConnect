from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Kit(Base):
    __tablename__ = 'kits'
    
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    k_type = Column(String(50))  # Espadín, Regalo, Degustacion, Variado
    description = Column(String(70))  # Descripción del kit

    # Relación con productos
    product = relationship('Product', back_populates='kit')
