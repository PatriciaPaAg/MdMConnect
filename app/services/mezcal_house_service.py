from app.repositories.mezcal_house_repo import MezcalHouseRepo


class MezcalHouseService:
    def __init__(self, mezcal_house_repo: MezcalHouseRepo):
        self.mezcal_house_repo = mezcal_house_repo

    def create_mezcal_house(self, mezcal_house_data: dict):
        required_fields = ['name', 'contactPerson', 'contactNumber']
        for field in required_fields:
            if field not in mezcal_house_data:
                raise ValueError(f"Missing field '{field}' in mezcal_house data.")
            
        return self.mezcal_house_repo.create_mezcal_house(mezcal_house_data)
    
    def get_all_mezcal_houses(self):
        return self.mezcal_house_repo.get_all_mezcal_houses()
    
    def get_mezcal_house_by_id(self, mezcal_house_id):
        return self.mezcal_house_repo.get_mezcal_house_by_id(mezcal_house_id)
    
    def update_mezcal_house(self, mezcal_house_id, name=None, contactPerson=None, contactNumber=None):
        mezcal_house = self.get_mezcal_house_by_id(mezcal_house_id)
        if not mezcal_house:
            raise ValueError(f"Mezcal house with ID {mezcal_house_id} not found.")
        
        return self.mezcal_house_repo.update_mezcal_house(mezcal_house_id, name, contactPerson, contactNumber)

    def delete_mezcal_house(self, mezcal_house_id):
        mezcal_house = self.get_mezcal_house_by_id(mezcal_house_id)
        if not mezcal_house:
            raise ValueError(f"Mezcal house with ID {mezcal_house_id} not found.")
        
        return self.mezcal_house_repo.delete_mezcal_house(mezcal_house_id)
    
