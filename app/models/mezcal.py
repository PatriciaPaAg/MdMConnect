from sqlalchemy import Column, Integer, String, REAL, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .base import Base
from .product import Product

class Mezcal(Base):
    __tablename__ = 'mezcals'
    
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    agave_type = Column(String(50), nullable=False)  # Espadín, Mexicano, Ensamble, etc.
    aging = Column(String(50), nullable=False)  # Joven, Reposado, Añejo
    detail = Column(String(50))  # Detalles adicionales, si es un ensamble
    alcohol_content = Column(REAL, CheckConstraint('alcohol_content BETWEEN 34 AND 60'))  # En porcentaje
    size_ml = Column(Integer, CheckConstraint('size_ml > 0'))

    # Relación con productos
    product = relationship('Product', back_populates='mezcal')
