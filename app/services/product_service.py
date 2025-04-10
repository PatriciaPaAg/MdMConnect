from app.repositories.product_repo import ProductRepo

class ProductService:
    def __init__(self, db_session):
        self.product_repo = ProductRepo(db_session)

    def create_product(self, data: dict):
        required_fields = ['p_type', 'brand_id', 'stock', 'price']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
            
        return self.product_repo.create_product(data)
    
    def get_all_products(self):
        return self.product_repo.get_all_products()
    
    def get_product_by_id(self, product_id: int):
        product = self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return product.to_dict()
    
    def update_product(self, product_id: int, data: dict):
        existing_product = self.product_repo.get_product_by_id(product_id)
        if not existing_product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return self.product_repo.update_product(existing_product, data)
    
    def delete_product(self, product_id: int):
        existing_product = self.product_repo.get_product_by_id(product_id)
        if not existing_product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return self.product_repo.delete_product(existing_product)