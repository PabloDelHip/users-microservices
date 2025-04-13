from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass
class Client:
    id: UUID
    name: str
    email: str
    phone: str
    active: bool  # active / inactive
    created_at: datetime
