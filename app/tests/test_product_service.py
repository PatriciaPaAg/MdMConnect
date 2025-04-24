# tests/test_product_service.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base  
from enums.product_enum import ProductType
from models.brand import Brand
from models.mezcal_house import MezcalHouse
from repositories.brand_repo import BrandRepo
from repositories.product_repo import ProductRepo
from services.product_service import ProductService
from repositories.mezcal_repo import MezcalRepo

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

@pytest.fixture
def product_service(db_session):
    brand_repo = BrandRepo(db_session)
    product_repo = ProductRepo(db_session)
    mezcal_repo = MezcalRepo(db_session)
    return ProductService(product_repo, brand_repo, mezcal_repo)

def test_create_product_valid(product_service, db_session):
    new_mezcal_house = MezcalHouse(name="Casa Mezcal Test", contactPerson="Juan", contactNumber="123456789")
    db_session.add(new_mezcal_house)
    db_session.commit()
    new_brand = Brand(name="Marca Test", mezcal_house_id=new_mezcal_house.id)
    db_session.add(new_brand)
    db_session.commit()

    data = {
        'p_type': ProductType.MEZCAL.value,
        'brand_id': new_brand.id,
        'stock': 5,
        'price': 350,
        'agave_type': 'Espadin',
        'aging': 'reposado',
        'alcohol_content': 35,
        'size_ml': 750,
        'detail': ''
    }

    product = product_service.create_product(data)
    # assert product.p_type == "mezcal"
    # assert product.price == 350
    # assert product.brand_id == new_brand.id

# def test_create_product_invalid_type(product_service, db_session):
#     new_brand = Brand(name="Marca Test", mezcal_house_id=1)
#     db_session.add(new_brand)
#     db_session.commit()

#     data = {
#         "p_type": "chocolate",  # no es un tipo válido
#         "brand_id": new_brand.id,
#         "price": 350,
#         "stock": 5
#     }

#     with pytest.raises(ValueError) as e:
#         product_service.create_product(data)
#     assert "Tipo de producto inválido" in str(e.value)

# def test_create_product_invalid_brand(product_service):
#     data = {
#         "p_type": ProductTypeEnum.MEZCAL.value,
#         "brand_id": 999,  # no existe
#         "price": 200,
#         "stock": 2
#     }

#     with pytest.raises(ValueError) as e:
#         product_service.create_product(data)
#     assert "Marca no encontrada" in str(e.value)
