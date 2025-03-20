from sqlalchemy.orm import Session
from models.base import Base, engine
from repositories.product_repository import ProductRepository
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

product_repo = ProductRepository(session)

new_product = product_repo.create_product(brand_id=1, stock=11, price=280.00)
print(f"Proudct created: {new_product}")

all_products = product_repo.get_all_products()
print(f"All products: {all_products}")

updated_product = product_repo.update_product(product_id=10, price=300.00)
print(f"Product updated: {updated_product}")

updated_product = product_repo.update_product(product_id=10, stock=300.00)
print(f"Product updated: {updated_product}")

deleted_product = product_repo.delete_product(product_id=10)
print(f"Product deleted: {deleted_product}")