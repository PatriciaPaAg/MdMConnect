from sqlalchemy.orm import Session
from models.alcoholic_drink import AlcoholicDrink

class AlcohoDrinkRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def create_alcoho_drink(self, product_id: int, ad_data: dict):
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
    
    def get_all_alcoho_drinks(self):
        return self.db_session.query(AlcoholicDrink).all()
    
    def get_alcoho_drink_by_id(self, ad_id):
        return self.db_session.query(AlcoholicDrink).filter(AlcoholicDrink.product_id == ad_id).first()
    
    def update_alcoho_drink(self, propduct_id, ad_type=None, flavour=None, alcohol_content=None, size_ml=None):
        alcoholic_drink = self.get_alcoho_drink_by_id(propduct_id)
        if alcoholic_drink:
            if ad_type is not None:
                alcoholic_drink.ad_type = ad_type
            if flavour is not None:
                alcoholic_drink.flavour = flavour
            if alcohol_content is not None:
                alcoholic_drink.alcohol_content = alcohol_content
            if size_ml is not None:
                alcoholic_drink.size_ml = size_ml
            self.db_session.commit()
            self.db_session.refresh(alcoholic_drink)
        return alcoholic_drink
    
    def delete_alcoho_drink(self, ad_id):
        alcoholic_drink = self.get_alcoho_drink_by_id(ad_id)
        if alcoholic_drink:
            self.db_session.delete(alcoholic_drink)
            self.db_session.commit()
        return alcoholic_drink
    