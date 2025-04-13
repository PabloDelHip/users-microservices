from fastapi import APIRouter, Depends, HTTPException
from app.core.services.agent_service import AgentService
from app.schemas.agent_schema import AgentResponse
from app.dependencies.agent import get_agent_service 

router = APIRouter()

@router.get("/", response_model=list[AgentResponse])
def get_agents():
    service = AgentService()
    return service.get()

@router.post("/", response_model=list[AgentResponse])
def add(service: AgentService = Depends(get_agent_service)):
    agents = service.add()
    return [AgentResponse(**agent.__dict__) for agent in agents]

@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent_by_id(agent_id: int):
    service = AgentService()
    agent = service.get_agent_by_id(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agente no encontrado")
    return agent
