import re
from pydantic import BaseModel, Field, field_validator

class EmailUser(BaseModel):

  value: str = Field(..., description="User name")

  @field_validator("value")
  def email_validate(cls, v):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not (bool(re.match(pattern, v))):
      raise ValueError("The email address is invalid.")
    
    return v

  def __str__(self):
    return self.value