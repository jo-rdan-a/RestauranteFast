from pydantic import BaseModel

class MesaCreate(BaseModel):
    numero: int
    capacidade: int

class Mesa(BaseModel):
    id: int
    numero: int
    capacidade: int

    class Config:
        from_attributes = True
