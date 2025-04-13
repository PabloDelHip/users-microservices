from app.domain.ports.user_repository import UserRepository
from app.domain.entities.user import User

class UserService:
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository

  def get_by_id(self, user_id: int) -> User:
    return self.user_repository.get_by_id(user_id)

  def get_by_email(self, email: str) -> User:
    return self.user_repository.get_by_email(email)

  def get_all(self, tenant_id: int) -> list[User]:
    return self.user_repository.get_all(tenant_id)

  def save(self, user: User) -> User:
    return self.user_repository.get_all(user)

  def update(self, user_id: int, user: User) -> User:
    return self.user_repository.update(user_id, user)

  def delete(self, user_id: int) -> bool:
    return self.user_repository.delete(user_id)