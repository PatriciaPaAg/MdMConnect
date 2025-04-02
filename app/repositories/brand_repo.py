from sqlalchemy.orm import Session
from models.brand import Brand

class BrandRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_brand(self, name: str, mezcal_house_id: int):
        new_brand = Brand(
            name=name,
            mezcal_house_id=mezcal_house_id
        )
        self.db_session.add(new_brand)
        self.db_session.commit()
        return new_brand
    
    def get_all_brands(self):
        return self.db_session.query(Brand).all()
    
    def get_brand_by_id(self, brand_id):
        return self.db_session.query(Brand).filter(Brand.id == brand_id).first()
    
    def update_brand(self, brand_id, name=None, mezcal_house_id=None):
        brand = self.get_brand_by_id(brand_id)
        if brand:
            if name is not None:
                brand.name = name
            if mezcal_house_id is not None:
                brand.mezcal_house_id = mezcal_house_id
            self.db_session.commit()
            self.db_session.refresh(brand)
        return brand
    
    def delete_brand(self, brand_id):
        brand = self.get_brand_by_id(brand_id)
        if brand:
            self.db_session.delete(brand)
            self.db_session.commit()
        return brand