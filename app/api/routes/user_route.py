from fastapi import APIRouter, Depends
from app.core.services.user_service import UserService
from app.domain.entities.user import User
from app.events.producers.user_event_producer import UserEventProducer

router = APIRouter()

# Crear un usuario
@router.post("/", response_model=User)
def create_user(name: str, email: str):
    service = UserService()
    return service.create_user(name, email)

# Obtener un usuario por ID (ficticio por ahora)
@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    service = UserService()
    return service.get_user_by_id(user_id)
