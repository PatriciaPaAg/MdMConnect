from sqlalchemy.orm import Session
from models.salt import Salt

class SaltRepo:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_salt(self, product_id: int, salt_data: dict):
        new_salt = Salt(
            product_id=product_id,
            s_type=salt_data['salt_type'],
            size_units=salt_data['size_units'],
        )
        self.db_session.add(new_salt)
        self.db_session.commit()
        return new_salt 

    def get_all_salts(self):
        return self.db_session.query(Salt).all()
    
    def get_salt_by_id(self, salt_id):
        return self.db_session.query(Salt).filter(Salt.product_id == salt_id).first()
    
    def update_salt(self, salt_id, salt_type=None, size_units=None):
        salt = self.get_salt_by_id(salt_id)
        if salt:
            if salt_type is not None:
                salt.salt_type = salt_type
            if size_units is not None:
                salt.size_units = size_units
            self.db_session.commit()
            self.db_session.refresh(salt)
        return salt

    def delete_salt(self, salt_id):
        salt = self.get_salt_by_id(salt_id)
        if salt:
            self.db_session.delete(salt)
            self.db_session.commit()
        return salt