from repositories.alcoho_drink_repo import AlcohoDrinkRepo
from repositories.product_repo import ProductRepo


class AlcohoDrinkService:
    def __init__(self, alcoho_drink_repo: AlcohoDrinkRepo):
        self.alcoho_drink_repo = alcoho_drink_repo

    def create_alcoho_drink(self, product_id: int, ad_data: dict):
        required_fields = ['ad_type', 'flavour', 'alcohol_content', 'size_ml']
        for field in required_fields:
            if field not in ad_data:
                raise ValueError(f"Missing field '{field}' in alcoholic drink data.")

        product = ProductRepo.get_product_by_id(product_id)
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found.")

        if ad_data['alcohol_content'] < 0 or ad_data['alcohol_content'] > 100:
            raise ValueError("Alcohol content must be between 0 and 100 percent.")

        if ad_data['size_ml'] <= 0:
            raise ValueError("Size in ml must be greater than 0.")

        return self.alcoho_drink_repo.create_alcoho_drink(product_id, ad_data)
    
    def get_all_alcoho_drinks(self):
        return self.alcoho_drink_repo.get_all_alcoho_drinks()
    
    def get_alcoho_drink_by_id(self, ad_id: int):
        alcoho_drink = self.alcoho_drink_repo.get_alcoho_drink_by_id(ad_id)
        if not alcoho_drink:
            raise ValueError(f"Alcoholic drink with product_id {ad_id} not found.")
        return alcoho_drink.to_dict()
    
    def update_alcoho_drink(self, ad_id: int, ad_type=None, flavour=None, alcohol_content=None, size_ml=None):
        alcoho_drink = self.get_alcoho_drink_by_id(ad_id)
        if not alcoho_drink:
            raise ValueError(f"Alcoholic drink with product_id {ad_id} not found.")

        if alcohol_content:
            if alcohol_content < 0 or alcohol_content > 100:
                raise ValueError("Alcohol content must be between 0 and 100 percent.")
        if size_ml:
            if size_ml <= 0:
                raise ValueError("Size in ml must be greater than 0.")

        return self.alcoho_drink_repo.update_alcoho_drink(ad_id, ad_type, flavour, alcohol_content, size_ml)

    def delete_alcoho_drink(self, ad_id: int):
        alcoho_drink = self.get_alcoho_drink_by_id(ad_id)
        if not alcoho_drink:
            raise ValueError(f"Alcoholic drink with product_id {ad_id} not found.")
        
        return self.alcoho_drink_repo.delete_alcoho_drink(ad_id)