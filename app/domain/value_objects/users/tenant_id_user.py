from pydantic import BaseModel, Field, field_validator

class TenantIdeUser(BaseModel):

  value: str = Field(..., description="User name")
  def tenant_id_user(cls, v):
    if not isinstance(v, int):
      raise ValueError("tenant id must be an integer")
    if v > 0:
      raise ValueError("Dede ser mayor a 0")

  def __str__(self):
    return self.value