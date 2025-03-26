from sqlalchemy.orm import Session
from models.base import Base, engine
from app.repositories.mezcal_house_repo import MezcalHouseRepository

Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

mezcal_house_repo = MezcalHouseRepository(session)

all_mezcals_houses = mezcal_house_repo.get_all_houses()
print(f"All mezcals: {all_mezcals_houses}")
