from pydantic import BaseModel, field_validator, Field

class NameUser(BaseModel):
    value: str = Field(..., description="User name")

    @field_validator("value")
    def name_validate(cls, v):
        v = v.strip()
        if len(v) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")

        if len(v) > 50:
            raise ValueError("El nombre no debe superar los 50 caracteres")

        if not v.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras y espacios")
        return v
    
    def __eq__(self, other):
        return isinstance(other, NameUser) and self.value == other.value

    def __str__(self):
      return self.value
