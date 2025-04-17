from repositories.salt_repo import SaltRepo
from repositories.product_repo import ProductRepo

class SaltService:
    def __init__(self, salt_repo: SaltRepo):
        self.salt_repo = salt_repo

    def create_salt(self, product_id: int, salt_data: dict):
        required_fields = ['salt_type', 'size_units']
        for field in required_fields:
            if field not in salt_data:
                raise ValueError(f"Missing field '{field}' in salt data.")
            
        product = ProductRepo.get_product_by_id(product_id)
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        return self.salt_repo.create_salt(product_id, salt_data)
    
    def get_all_salts(self):
        return self.salt_repo.get_all_salts()
    
    def get_salt_by_id(self, salt_id: int):
        salt = self.salt_repo.get_salt_by_id(salt_id)
        if not salt:
            raise ValueError(f"Salt with product_id {salt_id} not found.")
        return salt.to_dict()
    
    def update_salt(self, salt_id: int, salt_type=None, size_units=None):
        salt = self.get_salt_by_id(salt_id)
        if not salt:
            raise ValueError(f"Salt with product_id {salt_id} not found.")
        
        return self.salt_repo.update_salt(salt_id, salt_type, size_units)
    
    def delete_salt(self, salt_id: int):
        salt = self.get_salt_by_id(salt_id)
        if not salt:
            raise ValueError(f"Salt with product_id {salt_id} not found.")
        
        return self.salt_repo.delete_salt(salt_id)
    