from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Configuración de la conexión
USER = "mezcal_user"
PASSWORD = "mercado0499"
HOST = "localhost"
DATABASE = "mezcal_store" 

# Conexión a MySQL
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

# Motor para conectar con la base de datos
engine = create_engine(DATABASE_URL)

# Clase base para los modelos
Base = declarative_base()

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
