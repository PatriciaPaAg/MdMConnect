from repositories.brand_repo import BrandRepo
from app.repositories.mezcal_house_repo import MezcalHouseRepo


class BrandService:
    def __init__(self, brand_repo: BrandRepo):
        self.brand_repo = brand_repo

    def create_brand(self, name, mezcal_house_id):
        if not name or not mezcal_house_id:
            raise ValueError("Name and Mezcal House ID are required.")
        
        mezcal_house = MezcalHouseRepo.get_mezcal_house_by_id(mezcal_house_id)
        if mezcal_house is None:
            raise ValueError(f"Mezcal House with ID {mezcal_house_id} not found.")

        return self.brad_repo.create_brand(name, mezcal_house_id)

    def get_all_brands(self):
        return self.brand_repo.get_all_brands()
    
    def get_brand_by_id(self, brand_id):
        brand = self.brand_repo.get_brand_by_id(brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {brand_id} not found.")
        return brand.to_dict()
    
    def update_brand(self, brand_id, name=None, mezcal_house_id=None):
        brand = self.get_brand_by_id(brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {brand_id} not found.")
        
        if mezcal_house_id:
            mezcal_house = MezcalHouseRepo.get_mezcal_house_by_id(mezcal_house_id)
            if mezcal_house is None:
                raise ValueError(f"Mezcal House with ID {mezcal_house_id} not found.")
        
        return self.brand_repo.update_brand(brand_id, name, mezcal_house_id)
    
    def delete_brand(self, brand_id):
        brand = self.get_brand_by_id(brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {brand_id} not found.")
        return self.brand_repo.delete_brand(brand_id)