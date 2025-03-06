
from models.product import Product

class Kit(Product):
    def __init__(self, id, brand_id, price, stock, kit_type, description):
        super().__init__(id, brand_id, price, stock)
        self.kit_type = kit_type
        self.description = description

    def get_info(self):
        info = super().get_info()
        info.update({
            "kit_type": self.kit_type,
            "description": self.description
        })
        return info
