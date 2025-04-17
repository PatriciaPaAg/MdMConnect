from sqlalchemy.orm import Session
from models.mezcal_house import MezcalHouse

class MezcalHouseRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_mezcal_house(self, mezcal_house_data: dict):
        new_mezcal_house = MezcalHouse(
            name=mezcal_house_data['name'],
            contactPerson=mezcal_house_data.get('contactPerson'),
            contactNumber=mezcal_house_data.get('contactNumber')
        )

    def get_all_mezcal_houses(self):
        return self.db_session.query(MezcalHouse).all()
    
    def get_mezcal_house_by_id(self, mezcal_house_id):
        return self.db_session.query(MezcalHouse).filter(MezcalHouse.id == mezcal_house_id).first()
    
    def update_mezcal_house(self, mezcal_house_id, name=None, contactPerson=None, contactNumber=None):
        mezcal_house = self.get_mezcal_house_by_id(mezcal_house_id)
        if mezcal_house:
            if name is not None:
                mezcal_house.name = name
            if contactPerson is not None:
                mezcal_house.contactPerson = contactPerson
            if contactNumber is not None:
                mezcal_house.contactNumber = contactNumber
            self.db_session.commit()
            self.db_session.refresh(mezcal_house)
        return mezcal_house
    
    def delete_mezcal_house(self, mezcal_house_id):
        mezcal_house = self.get_mezcal_house_by_id(mezcal_house_id)
        if mezcal_house:
            self.db_session.delete(mezcal_house)
            self.db_session.commit()
        return mezcal_house
    
