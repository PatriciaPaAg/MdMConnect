from sqlalchemy.orm import Session
from models.stock_movements import StockMovement

class StockMvtsRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_stock_mvement(self, product_id: int, stock_movement_data: dict):
        new_stock_movement = StockMovement(
            product_id=product_id,
            movement_type=stock_movement_data['movement_type'],
            quantity=stock_movement_data['quantity']
        )
        self.db_session.add(new_stock_movement)
        self.db_session.commit()
        return new_stock_movement
    
    def get_all_stock_movements(self):
        return self.db_session.query(StockMovement).all()
    
    def get_stock_movement_by_id(self, stock_movement_id):
        return self.db_session.query(StockMovement).filter(StockMovement.id == stock_movement_id).first()
    
    def update_stock_movement(self, stock_movement_id, movement_type=None, quantity=None):
        stock_movement = self.get_stock_movement_by_id(stock_movement_id)
        if stock_movement:
            if movement_type is not None:
                stock_movement.movement_type = movement_type
            if quantity is not None:
                stock_movement.quantity = quantity
            self.db_session.commit()
            self.db_session.refresh(stock_movement)
        return stock_movement
    
    def delete_stock_movement(self, stock_movement_id): 
        stock_movement = self.get_stock_movement_by_id(stock_movement_id)
        if stock_movement:
            self.db_session.delete(stock_movement)
            self.db_session.commit()
        return stock_movement
    
    