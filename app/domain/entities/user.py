from pydantic import BaseModel, Field
from datetime import datetime
from app.domain.value_objects.users.name_user import NameUser
from app.domain.value_objects.users.email_user import EmailUser
from app.domain.value_objects.users.tenant_id_user import TenantIdeUser
# from app.domain.enums.user_type_enum import UserType

class User(BaseModel):
    id: int = Field(..., description="Id del producto")
    # tenant_id: TenantIdeUser
    name: NameUser
    email: EmailUser
    password: str
    # type: UserType
    # status: bool
    # created_at: datetime
    # updated_at: datetime