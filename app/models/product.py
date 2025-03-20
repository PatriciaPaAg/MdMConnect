from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='CASCADE'))
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, default=0)

    # Relación con la tabla Brands
    brand = relationship('Brand', back_populates='products')

    # Relación con otras tablas específicas
    alcoholic_drink = relationship('AlcoholicDrink', uselist=False, back_populates='product')
    craft = relationship('Craft', uselist=False, back_populates='product')
    kit = relationship('Kit', uselist=False, back_populates='product')
    mezcal = relationship('Mezcal', uselist=False, back_populates='product')
    salt = relationship('Salt', uselist=False, back_populates='product')
