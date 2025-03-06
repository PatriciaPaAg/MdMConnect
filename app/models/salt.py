
from models.product import Product

class Salt(Product):
    def __init__(self, id, brand_id, price, stock, salt_type, size, units):
        super().__init__(id, brand_id, price, stock)
        self.salt_type = salt_type
        self.size = size
        self.units = units

    def get_info(self):
        info = super().get_info()
        info.update({
            'salt_type': self.salt_type,
            'size': self.size,
            'units': self.units
        })
        return info
    