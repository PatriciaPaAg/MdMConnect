from repositories.kit_repo import KitRepo
from repositories.product_repo import ProductRepo

class KitService:
    def __init__(self, kit_repo: KitRepo):
        self.kit_repo = kit_repo

    def create_kit(self, product_id: int, kit_data: dict):
        required_fields = ['k_type', 'description']
        for field in required_fields:
            if field not in kit_data:
                raise ValueError(f"Missing field '{field}' in kit data.")
        product = ProductRepo.get_product_by_id(product_id)
        
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        return self.kit_repo.create_kit(product_id, kit_data)
    
    def get_all_kits(self):
        return self.kit_repo.get_all_kits()
    
    def get_kit_by_id(self, kit_id: int):
        kit = self.kit_repo.get_kit_by_id(kit_id)
        if not kit:
            raise ValueError(f"Kit with product_id {kit_id} not found.")
        return kit.to_dict()
    
    def update_kit(self, kit_id: int, k_type=None, description=None):
        kit = self.get_kit_by_id(kit_id)
        if not kit:
            raise ValueError(f"Kit with product_id {kit_id} not found.")

        return self.kit_repo.update_kit(kit_id, k_type, description)
    
    def delete_kit(self, kit_id: int):
        kit = self.get_kit_by_id(kit_id)
        if not kit:
            raise ValueError(f"Kit with product_id {kit_id} not found.")
        
        return self.kit_repo.delete_kit(kit_id)