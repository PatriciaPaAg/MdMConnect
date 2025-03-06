
from models.product import Product

class Craft(Product):
    def __init__(self, id, brand_id, price, stock, craft_type, material, size):
        super().__init__(id, brand_id, price, stock)
        self.craft_type = craft_type
        self.material = material
        self.size = size

    def get_info(self):
        info = super().get_info()
        info.update({
            "craft_type": self.craft_type,
            "material": self.material,
            "size": self.size
        })
        return info
