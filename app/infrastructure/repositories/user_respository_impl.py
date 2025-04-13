from app.infrastructure.repositories.database.db_connection_postgres import db
from app.infrastructure.repositories.database.models.user_model import UserModel
from app.domain.value_objects.users.name_user import NameUser
from app.domain.value_objects.users.email_user import EmailUser
from app.domain.ports.user_repository import UserRepository
from app.domain.entities.user import User
from typing import Optional, List

class UserRepositoryImpl(UserRepository):

  def __init__(self):
    self.session = db.get_session()
      
  def get_by_id(self, user_id: int) -> Optional[User]:
    pass

  def get_by_email(self, email: str) -> Optional[User]:
    pass

  
  def get_all(self, tenant_id: int) -> List[User]:
    users_db = self.session.query(UserModel).all()
    return [
        User(
            id=user.id,
            name=NameUser(value=user.name),
            email=EmailUser(value=user.email),
            password=user.password
        )
        for user in users_db
    ]

  
  def save(self, user: User) -> User:
    pass

  
  def update(self, user_id: int, user: User) -> Optional[User]:
    pass

  
  def delete(self, user_id: int) -> bool:
    pass