from sqlalchemy.orm import Session
from models.mezcal import Mezcal

class MezcalRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_mezcal(self, product_id: int, mezcal_data: dict):
        new_mezcal = Mezcal(
            product_id=product_id,
            agave_type=mezcal_data['agave_type'],
            aging=mezcal_data['aging'],
            detail=mezcal_data['detail'],
            alcohol_content=mezcal_data['alcohol_content'],
            size_ml=mezcal_data['size_ml']
        )
        self.db_session.add(new_mezcal)
        self.db_session.commit()
        return new_mezcal 

    def get_all_mezcals(self):
        return self.db_session.query(Mezcal).all()
    
    def get_mezcal_by_id(self, mezcal_id):
        return self.db_session.query(Mezcal).filter(Mezcal.product_id == mezcal_id).first()
    
    def update_mezcal(self, mezcal_id, agave_type=None, aging=None, detail=None, alcohol_content=None, size_ml=None):
        mezcal = self.get_mezcal_by_id(mezcal_id)
        if mezcal:
            if agave_type is not None:
                mezcal.agave_type = agave_type
            if aging is not None:
                mezcal.aging = aging
            if detail is not None:
                mezcal.detail = detail
            if alcohol_content is not None:
                mezcal.alcohol_content = alcohol_content
            if size_ml is not None:
                mezcal.size_ml = size_ml
            self.db_session.commit()
            self.db_session.refresh(mezcal)
        return mezcal

    def delete_mezcal(self, mezcal_id):
        mezcal = self.get_mezcal_by_id(mezcal_id)
        if mezcal:
            self.db_session.delete(mezcal)
            self.db_session.commit()
        return mezcal
    
