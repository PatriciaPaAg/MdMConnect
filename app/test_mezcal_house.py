from sqlalchemy.orm import Session
from models.base import Base, engine
from app.repositories.mezcl_haus_repo import MzcalHausRepo

Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

mezcl_haus_repo = MzcalHausRepo(session)

all_mezcals_houses = mezcl_haus_repo.get_all_houses()
print(f"All mezcals: {all_mezcals_houses}")
