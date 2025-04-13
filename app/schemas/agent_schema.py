from pydantic import BaseModel, EmailStr
from typing import Optional
from app.domain.enums.agent_role_enum import AgentRoleEnum

class AgentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[AgentRoleEnum] = AgentRoleEnum.AGENT
    company: int
    active: Optional[bool] = True

class AgentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: AgentRoleEnum
    company: int
    active: bool
