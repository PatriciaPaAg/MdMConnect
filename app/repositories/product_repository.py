from sqlalchemy.orm import Session
from models.product import Product

class ProductRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_product(self, brand_id, stock, price):
        new_product = Product(
            brand_id=brand_id,
            stock=stock,
            price=price
        )
        self.db_session.add(new_product)
        self.db_session.commit()
        self.db_session.refresh(new_product)
        return new_product
    
    def get_all_products(self):
        print('Aqui we......')
        return self.db_session.query(Product).all()
    
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