from sqlalchemy.orm import Session
from models.mezcal_house import MezcalHouse

class MezcalHouseRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_houses(self):
        print('Aqui we......')
        return self.db_session.query(MezcalHouse).all()
