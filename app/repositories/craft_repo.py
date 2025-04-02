from sqlalchemy.orm import Session
from models.craft import Craft

class CraftRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_craft(self, product_id: int, craft_data: dict):
        new_craft = Craft(
            product_id=product_id,
            c_type=craft_data['c_type'],
            material=craft_data['material'],
            size=craft_data['size']
        )
        self.db_session.add(new_craft)
        self.db_session.commit()
        return new_craft 

    def get_all_crafts(self):
        return self.db_session.query(Craft).all()
    
    def get_craft_by_id(self, craft_id):
        return self.db_session.query(Craft).filter(Craft.product_id == craft_id).first()
    
    def update_craft(self, craft_id, c_type=None, material=None, size=None):
        craft = self.get_craft_by_id(craft_id)
        if craft:
            if c_type is not None:
                craft.c_type = c_type
            if material is not None:
                craft.material = material
            if size is not None:
                craft.size = size
            self.db_session.commit()
            self.db_session.refresh(craft)
        return craft

    def delete_craft(self, craft_id):
        craft = self.get_craft_by_id(craft_id)
        if craft:
            self.db_session.delete(craft)
            self.db_session.commit()
        return craft