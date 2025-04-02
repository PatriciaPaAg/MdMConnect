from sqlalchemy.orm import Session
from models.product import Product, ProductType
from .mezcal_repo import MezcalRepo

class ProductRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_product(self, product_data: dict):

        p_type = product_data.get("p_type")

        new_product = Product(
            p_type = p_type,
            brand_id = product_data['brand_id'],
            stock = product_data['stock'],
            price = product_data['price']
        )
        self.db_session.add(new_product)
        self.db_session.commit()

        if p_type == ProductType.MEZCAL.value:
            return MezcalRepo(self.db_session).create_mezcal(new_product.id, product_data)

        return new_product
    
    def get_all_products(self):
        products = self.db_session.query(Product).all()
        return [product.to_dict() for product in products]
        # return self.db_session.query(Product).all()
    
    def get_product_by_id(self, product_id):
        return self.db_session.query(Product).filter(Product.id == product_id).first()
    
    def update_product(self, product_id, price=None, stock=None):
        product = self.get_product_by_id(product_id)
        if product:
            if price is not None:
                product.price = price
            if stock is not None:
                product.stock = stock
            self.db_session.commit()
            self.db_session.refresh(product)
        return product
    
    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.db_session.delete(product)
            self.db_session.commit()
        return product