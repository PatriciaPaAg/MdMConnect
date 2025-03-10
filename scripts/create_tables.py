from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, DateTime, REAL
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

# Definir la base de datos
Base = declarative_base()

# Definir las tablas (entidades)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    rol = Column(String(20))

class MezcalHouse(Base):
    __tablename__ = 'mezcal_houses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    contactPerson = Column(String(50))
    contactNumber = Column(String(10))

    # Relación con brands
    brands = relationship('Brand', back_populates='mezcal_house')
    
class Brand(Base):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    mezcal_house_id = Column(Integer, ForeignKey('mezcal_houses.id'))

    # Relación con mezcal_houses
    mezcal_house = relationship('MezcalHouse', back_populates='brands')

    # Relación con productos
    products = relationship('Product', back_populates='brand')

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, default=0)

    # Relación con la tabla Brand
    brand = relationship('Brand', back_populates='products')

    # Relación con otras tablas específicas
    alcoholic_drink = relationship('AlcoholicDrink', uselist=False, back_populates='product')
    craft = relationship('Craft', uselist=False, back_populates='product')
    kit = relationship('Kit', uselist=False, back_populates='product')
    mezcal = relationship('Mezcal', uselist=False, back_populates='product')
    salt = relationship('Salt', uselist=False, back_populates='product')

class InventoryMovement(Base):
    __tablename__ = 'inventory_movements'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    movement_type = Column(String(50))  # 'entrada' o 'salida'
    quantity = Column(Integer)
    date = Column(DateTime, default=func.now())

    # Relación con productos
    product = relationship('Product')

class AlcoholicDrink(Base):
    __tablename__ = 'alcoholic_drinks'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    ad_type = Column(String(50))  # Cream, liquor, cocktail, gin
    flavour = Column(String(50))
    alcohol_content = Column(REAL)  # Porcentaje de alcohol
    size_ml = Column(Integer, nullable=False)

    # Relación con productos
    product = relationship('Product', back_populates='alcoholic_drink')

class Craft(Base):
    __tablename__ = 'crafts'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    craft_type = Column(String(50))  # Ej. caballito, cuchara, botella pintada, etc.
    material = Column(String(50))  # Madera, barro, etc.
    size = Column(String(50))  # Chico, mediano, etc.

    # Relación con productos
    product = relationship('Product', back_populates='craft')

class Kit(Base):
    __tablename__ = 'kits'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    k_type = Column(String(50))  # Espadín, Regalo, Degustacion, Variado
    description = Column(String(70))  # Descripción del kit

    # Relación con productos
    product = relationship('Product', back_populates='kit')

class Mezcal(Base):
    __tablename__ = 'mezcals'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    agave_type = Column(String(50))  # Espadín, Mexicano, etc.
    aging = Column(String(50))  # Joven, Reposado, Añejo
    detail = Column(String(50))  # Detalles adicionales, si es un ensamble
    alcohol_content = Column(REAL)  # En porcentaje
    size_ml = Column(Integer, nullable=False)

    # Relación con productos
    product = relationship('Product', back_populates='mezcal')

class Salt(Base):
    __tablename__ = 'salts'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    type = Column(String(50))  # Gusano, chapulín, etc.
    size = Column(Integer)  # Tamaño
    units = Column(String(50))  # Unidades (gr, oz, etc.)

    # Relación con productos
    product = relationship('Product', back_populates='salt')


# Configuración de la conexión
USER = "mezcal_user"
PASSWORD = "mercado0499"
HOST = "localhost"
DATABASE = "mezcal_store" 

# Crear la conexión
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)
