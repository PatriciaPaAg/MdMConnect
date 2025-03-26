from sqlalchemy.orm import Session
from models.alcoholic_drink import AlcoholicDrink

class AlcoholicDrinkRepo:
    def __init__(self):
        self.db_session = Session

    def create_alcoholic_drink(self, product_id: int, ad_data: dict):
        new_alcoholic_drink = AlcoholicDrink(
            product_id=product_id,
            ad_type=ad_data['ad_type'],
            flavour=ad_data['flavour'],
            alcohol_content=ad_data['alcohol_content'],
            size_ml=ad_data['size_ml']
        )
        self.db_session.add(new_alcoholic_drink)
        self.db_session.commit()
        return new_alcoholic_drink