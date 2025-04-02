from sqlalchemy.orm import Session
from models.kit import Kit

class KitRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_kit(self, product_id: int, kit_data: dict):
        new_kit = Kit(
            product_id=product_id,
            k_type=kit_data['k_type'],
            description=kit_data['description']
        )
        self.db_session.add(new_kit)
        self.db_session.commit()
        return new_kit 

    def get_all_kits(self):
        return self.db_session.query(Kit).all()
    
    def get_kit_by_id(self, kit_id):
        return self.db_session.query(Kit).filter(Kit.product_id == kit_id).first()
    
    def update_kit(self, kit_id, k_type=None, description=None):
        kit = self.get_kit_by_id(kit_id)
        if kit:
            if k_type is not None:
                kit.k_type = k_type
            if description is not None:
                kit.description = description
            self.db_session.commit()
            self.db_session.refresh(kit)
        return kit

    def delete_kit(self, kit_id):
        kit = self.get_kit_by_id(kit_id)
        if kit:
            self.db_session.delete(kit)
            self.db_session.commit()
        return kit