from sqlalchemy.orm import Session
from models.base import Base, engine
from repositories.product_repo import ProductRepo
# from models.mezcal_house import MezcalHouse
# from models.brand import Brand
# from models.product import Product
# from models.alcoholic_drink import AlcoholicDrink
# from models.craft import Craft
# from models.kit import Kit
# from models.mezcal import Mezcal
# from models.salt import Salt
# from models.stock_movement import StockMovement

Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

product_repo = ProductRepo(session)

# mezcal_data = {
#     "p_type": "mezcal",
#     "brand_id": 1,
#     "stock": 12,
#     "price": 280.00,
#     "agave_type": "Espadin",
#     "aging": "Joven",
#     "detail": "Gusano",
#     "alcohol_content": 41.0,
#     "size_ml": 750
#     }


# new_mezcal = product_repo.create_product(mezcal_data)
# print(f"Proudct created: {new_mezcal}")

all_products = product_repo.get_all_products()
print(f"All products: {all_products}")

# updated_product = product_repo.update_product(product_id=10, price=300.00)
# print(f"Product updated: {updated_product}")

# updated_product = product_repo.update_product(product_id=10, stock=300.00)
# print(f"Product updated: {updated_product}")

# deleted_product = product_repo.delete_product(product_id=10)
# print(f"Product deleted: {deleted_product}")