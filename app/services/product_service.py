from app.repositories.product_repo import ProductRepo
from enums.product_enum import ProductType
from repositories.brand_repo import BrandRepo



# ################# ADDDDDD VALID PRODUCT TYPES AND LOGICCCCCCC ######################
# ################# ADDDDDD VALID PRODUCT TYPES AND LOGICCCCCCC ######################      
# ################# ADDDDDD VALID PRODUCT TYPES AND LOGICCCCCCC ######################
# ################# ADDDDDD VALID PRODUCT TYPES AND LOGICCCCCCC ######################

class ProductService:
    def __init__(self, db_session):
        self.product_repo = ProductRepo(db_session)

    def create_product(self, data: dict):
        required_fields = ['p_type', 'brand_id', 'stock', 'price']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
            
        p_type = data.get('p_type')
        if p_type not in [ptype.value for ptype in ProductType]:
            raise ValueError(f"Invalid product type: {p_type}. Must be one of {[ptype.value for ptype in ProductType]}.")
        
        brand_id = BrandRepo.get_brand_by_id(data['brand_id'])
        if brand_id is None:
            raise ValueError(f"Brand with ID {data['brand_id']} not found.")

        if data['stock'] < 0:
            raise ValueError("Stock cannot be negative.")
        
        if data['price'] < 0:
            raise ValueError("Price cannot be negative.")
            
        return self.product_repo.create_product(data)
    
    def get_all_products(self):
        return self.product_repo.get_all_products()
    
    def get_product_by_id(self, product_id: int):
        product = self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return product.to_dict()
    
    def update_product(self, product_id: int, stock=None, price=None):
        product = self.get_product_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        if stock:
            if stock < 0:
                raise ValueError("Stock cannot be negative.")
        if price:
            if price < 0:
                raise ValueError("Price cannot be negative.")
        
        return self.product_repo.update_product(product_id, stock, price)

    def delete_product(self, product_id: int):
        existing_product = self.product_repo.get_product_by_id(product_id)
        if not existing_product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return self.product_repo.delete_product(existing_product)