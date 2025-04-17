from repositories.craft_repo import CraftRepo
from repositories.product_repo import ProductRepo
from enums.craft_enum import CraftSize


class CraftService:
    def __init__(self, craft_repo: CraftRepo):
        self.craft_repo = craft_repo

    def create_craft(self, product_id: int, craft_data: dict):
        required_fields = ['c_type', 'material', 'size']
        for field in required_fields:
            if field not in craft_data:
                raise ValueError(f"Missing field '{field}' in craft data.")

        product = ProductRepo.get_product_by_id(product_id)
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found.")

        size = craft_data['size']
        if size not in [c_size for c_size in CraftSize]:
            raise ValueError(f"Invalid size: {size}. Must be one of {[size.value for size in CraftSize]}.")
        
        return self.craft_repo.create_craft(product_id, craft_data)
    
    def get_all_crafts(self):
        return self.craft_repo.get_all_crafts()
    
    def get_craft_by_id(self, craft_id: int):
        craft = self.craft_repo.get_craft_by_id(craft_id)
        if not craft:
            raise ValueError(f"Craft with product_id {craft_id} not found.")
        return craft.to_dict()
    
    def update_craft(self, craft_id: int, c_type=None, material=None, size=None):
        craft = self.get_craft_by_id(craft_id)
        if not craft:
            raise ValueError(f"Craft with product_id {craft_id} not found.")
        
        # Validate the field detail, if the size is 'Ensamble'
        if size:
            if size not in [c_size for c_size in CraftSize]:
                raise ValueError(f"Invalid size: {size}. Must be one of {[size.value for size in CraftSize]}.")
        
        return self.craft_repo.update_craft(craft_id, c_type, material, size)
    
    def delete_craft(self, craft_id: int):
        craft = self.get_craft_by_id(craft_id)
        if not craft:
            raise ValueError(f"Craft with product_id {craft_id} not found.")
        
        return self.craft_repo.delete_craft(craft_id)