from models.base import Base, engine
from models.mezcal_house import MezcalHouse
from models.brand import Brand
from models.product import Product
from models.alcoholic_drink import AlcoholicDrink
from models.craft import Craft
from models.kit import Kit
from models.mezcal import Mezcal
from models.salt import Salt
from models.inventory_movement import InventoryMovement

def create_tables():
    print("Baking the tables...")
    Base.metadata.create_all(engine)
    print("Tables baked!")

if __name__ == "__main__":
    create_tables()
