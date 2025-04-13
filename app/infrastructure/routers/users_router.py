from fastapi import APIRouter, Depends
from typing import List
from app.domain.entities.user import User
from app.infrastructure.repositories.user_respository_impl import UserRepositoryImpl
from app.application.services.user_service import UserService

router = APIRouter()

def get_user_service():
  repository = UserRepositoryImpl()
  return UserService(repository)

@router.get("/", response_model=List[User])
def obtener_usuarios(service: UserService = Depends(get_user_service)):
    return service.get_all(1)