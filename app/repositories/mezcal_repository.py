from sqlalchemy.orm import Session
from models.mezcal import Mezcal

class MezcalRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_mezcals(self):
        print('Aqui we......')
        return self.db_session.query(Mezcal).all()
