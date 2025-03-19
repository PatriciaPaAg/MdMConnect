from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class AlcoholicDrink(Base):
    __tablename__ = 'alcoholic_drinks'
    
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    ad_type = Column(String(50))  # Cream, liquor, cocktail, gin
    flavour = Column(String(50))
    alcohol_content = Column(REAL)  # Porcentaje de alcohol
    size_ml = Column(Integer, nullable=False)

    # Relación con productos
    product = relationship('Product', back_populates='alcoholic_drink')
