from repositories.mezcal_repo import MezcalRepo
from sqlalchemy.exc import SQLAlchemyError
from enums.mezcal_enum import MezcalAging

# ################# ADDDDDD VALID AGING AND LOGICCCCCCC ######################

class MezcalService:
    def __init__(self, mezcal_repo: MezcalRepo):
        self.mezcal_repo = mezcal_repo

    def create_mezcal(self, product_id: int, mezcal_data: dict):
        required_fields = ['agave_type', 'aging', 'alcohol_content', 'size_ml']
        for field in required_fields:
            if field not in mezcal_data:
                raise ValueError(f"Missing field '{field}' in mezcal data.")
        
        # Validate the field detail, if the agave_type is 'Ensamble'
        agave_type = mezcal_data['agave_type']
        detail = mezcal_data.get('detail')
        if agave_type == 'Ensamble' and not detail:
            raise ValueError("Detail is required when agave_type is 'Ensamble'.") 
        aging = mezcal_data['aging']
        if aging not in [m_aging for m_aging in MezcalAging]:
            raise ValueError(f"Invalid aging type: {aging}. Must be one of {[aging.value for aging in MezcalAging]}.")
        
        if mezcal_data['alcohol_content'] < 35 or mezcal_data['alcohol_content'] > 55:
            raise ValueError("Alcohol content must be between 35 and 55 percent.")
        
        if mezcal_data['size_ml'] <= 0:
            raise ValueError("Size in ml must be greater than 0.")

        return self.mezcal_repo.create_mezcal(product_id, mezcal_data)

    def get_all_mezcals(self):
        return self.mezcal_repo.get_all_mezcals()

    def get_mezcal_by_id(self, mezcal_id: int):
        mezcal = self.mezcal_repo.get_mezcal_by_id(mezcal_id)
        if not mezcal:
            raise ValueError(f"Mezcal with product_id {mezcal_id} not found.")
        return mezcal

    def update_mezcal(self, mezcal_id: int, agave_type=None, aging=None, detail=None, alcohol_content=None, size_ml=None):
        mezcal = self.get_mezcal_by_id(mezcal_id)
        if not mezcal:
            raise ValueError(f"Mezcal with product_id {mezcal_id} not found.")

        # Validate the field detail, if the agave_type is 'Ensamble'
        if agave_type == 'Ensamble' or mezcal.agave_type == 'Ensamble':
            if not detail:
                raise ValueError("Detail is required when agave_type is 'Ensamble'.")
        if aging:
            if aging not in [m_aging for m_aging in MezcalAging]:
                raise ValueError(f"Invalid aging type: {aging}. Must be one of {[aging.value for aging in MezcalAging]}.")
        if alcohol_content:
            if alcohol_content < 35 or alcohol_content > 55:
                raise ValueError("Alcohol content must be between 35 and 55 percent.")
        if size_ml:
            if size_ml <= 0:
                raise ValueError("Size in ml must be greater than 0.")

        return self.mezcal_repo.update_mezcal(mezcal_id, agave_type, aging, detail, alcohol_content, size_ml)

    def delete_mezcal(self, mezcal_id: int):
        mezcal = self.mezcal_repo.get_mezcal_by_id(mezcal_id)
        if not mezcal:
            raise ValueError(f"Mezcal with product_id {mezcal_id} not found.")
        return self.mezcal_repo.delete_mezcal(mezcal_id)
