from repositories.mezcal_repo import MezcalRepo
from sqlalchemy.exc import SQLAlchemyError

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
        agave_type = mezcal_data.get('agave_type')
        detail = mezcal_data.get('detail')
        if agave_type == 'Ensamble' and not detail:
            raise ValueError("Detail is required when agave_type is 'Ensamble'.")        
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
        
        if agave_type:
            mezcal.agave_type = agave_type
        if aging:
            mezcal.aging = aging
        if alcohol_content:
            mezcal.alcohol_content = alcohol_content
        if size_ml:
            mezcal.size_ml = size_ml

        # Validate the field detail, if the agave_type is 'Ensamble'
        if agave_type == 'Ensamble' or mezcal.agave_type == 'Ensamble':
            if not detail:
                raise ValueError("Detail is required when agave_type is 'Ensamble'.")
        
        if detail:
            mezcal.detail = detail

        try:
            self.db_session.commit()
            self.db_session.refresh(mezcal)
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise RuntimeError(f"Error updating mezcal: {str(e)}")
        
        return mezcal

    def delete_mezcal(self, mezcal_id: int):
        mezcal = self.mezcal_repo.get_mezcal_by_id(mezcal_id)
        if not mezcal:
            raise ValueError(f"Mezcal with product_id {mezcal_id} not found.")
        return self.mezcal_repo.delete_mezcal(mezcal_id)
