from sqlalchemy.orm import Session
from models.base import Base, engine
from app.repositories.mezcal_repo import MezcalRepository
# from models.mezcal_house import MezcalHouse
# from models.brand import Brand
# from models.product import Product
# from models.alcoholic_drink import AlcoholicDrink
# from models.craft import Craft
# from models.kit import Kit
# from models.mezcal import Mezcal
# from models.salt import Salt
# from models.inventory_movement import InventoryMovement

Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

mezcal_repo = MezcalRepository(session)

# new_product = product_repo.create_product(brand_id=1, stock=11, price=280.00)
# print(f"Proudct created: {new_product}")

all_mezcals = mezcal_repo.get_all_mezcals()
print(f"All mezcals: {all_mezcals}")
