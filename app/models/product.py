
class Product:
    def __init__(self, id, brand_id, price, stock):
        self.id = id
        self.brand_id = brand_id
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        self.stock += quantity
    
    def get_info(self):
        return{
            'id': self.id,
            'brand_id': self.brand_id,
            'price': self.price,
            'stock': self.stock
        }