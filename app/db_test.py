from sqlalchemy import create_engine

# Configuración de la conexión
USER = "mezcal_user"
PASSWORD = "mercado0499"
HOST = "localhost"
DATABASE = "mezcal_store"

# Crear la conexión
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(DATABASE_URL)

# Probar la conexión
try:
    with engine.connect() as connection:
        print("✅ Conexión exitosa a MySQL.")
except Exception as e:
    print("❌ Error al conectar con MySQL:", e)
