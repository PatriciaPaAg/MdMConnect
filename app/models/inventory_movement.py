from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class InventoryMovement(Base):
    __tablename__ = 'inventory_movements'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))
    movement_type = Column(String(50))  # 'entrada' o 'salida'
    quantity = Column(Integer)
    date = Column(DateTime, default=func.now())

    # Relación con productos
    product = relationship('Product')
