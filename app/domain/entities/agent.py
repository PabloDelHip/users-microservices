from pydantic import BaseModel, EmailStr
from app.domain.enums.agent_role_enum import AgentRoleEnum
from datetime import datetime

class Agent(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    role: AgentRoleEnum
    company: int
    active: bool = True
    created_at: datetime
    updated_at: datetime
