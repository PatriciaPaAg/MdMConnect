from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, String
from sqlalchemy.orm import relationship
from .base import Base
from enum import Enum

class ProductType(Enum):
    MEZCAL = 'mezcal'
    ALCOHOLIC_DRINK = 'alcoholic_drink'
    CRAFT = 'craft'
    SALT = 'salt'
    KIT = 'kit'

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    p_type = Column(String(20), nullable=False)  # Tipo de producto
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='CASCADE'), nullable=False)
    stock = Column(Integer, default=0)
    price = Column(DECIMAL(10, 2), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'p_type': self.p_type,
            'brand_id': self.brand_id,
            'stock': self.stock,
            'price': float(self.price)  
        }

    # Relación con la tabla Brands
    brand = relationship('Brand', back_populates='product')

    # Relación con otras tablas específicas
    alcoholic_drink = relationship('AlcoholicDrink', uselist=False, back_populates='product')
    craft = relationship('Craft', uselist=False, back_populates='product')
    kit = relationship('Kit', uselist=False, back_populates='product')
    mezcal = relationship('Mezcal', uselist=False, back_populates='product')
    salt = relationship('Salt', uselist=False, back_populates='product')
 