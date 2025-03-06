
from models.product import Product

class Mezcal(Product):
    def __init__(self, id, brand_id, price, stock, agave_type, aging, alcohol_content):
        super().__init__(id, brand_id, price, stock)
        self.agave_type = agave_type
        self.aging = aging
        self.alcohol_content = alcohol_content

    def get_info(self):
        info = super().get_info()
        info.update({
            'agave_type': self.agave_type,
            'aging': self.aging,
            'alcohol_content': self.alcohol_content
        })
        return info
