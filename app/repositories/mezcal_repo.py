from sqlalchemy.orm import Session
from models.mezcal import Mezcal

class MezcalRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_mezcal(self, product_id: int, mezcal_data: dict):
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
        print('Aqui we......')
        return self.db_session.query(Mezcal).all()
    
    def get_mezcal_by_id(self, mezcal_id):
        return self.db_session.query(Mezcal).filter(Mezcal.product_id == mezcal_id).first()
    

