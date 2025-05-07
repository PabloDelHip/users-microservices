from pydantic import BaseModel, Field
from pydantic_core import core_schema

class TenantIdeUser(BaseModel):
    value: int = Field(..., description="Tenant id")

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.int_schema()  # Esto dice: "espera un entero como input"
        )

    @classmethod
    def _validate(cls, v: int):
        if not isinstance(v, int):
            raise TypeError("El tenant_id debe ser un entero")
        if v <= 0:
            raise ValueError("El tenant_id debe ser mayor a 0")
        return cls(value=v)

    def __str__(self):
        return str(self.value)
