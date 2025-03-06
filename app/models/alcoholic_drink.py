
from models.product import Product

class AlcoholicDrink(Product):
    def __init__(self, id, brand_id, price, stock, drink_type, flavour, alcohol_content, size_ml):
        super().__init__(id, brand_id, price, stock)
        self.drink_type = drink_type
        self.flavour = flavour
        self.alcohol_content = alcohol_content
        self.size_ml = size_ml

    def get_info(self):
        info = super().get_info()
        info.update({
            'drink_type': self.drink_type,
            'flavour': self.flavour,
            'alcohol_content': self.alcohol_content,
            'size_ml': self.size_ml
        })
        return info
    