from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReservaCreate(BaseModel):
    """Schema para criação de uma nova reserva."""
    nome_cliente: str
    mesa_id: int
    data_reserva: datetime
    numero_pessoas: int

    class Config:
        orm_mode = True

class ReservaOut(BaseModel):
    """Schema para retornar uma reserva existente."""
    id: int
    nome_cliente: str
    mesa_id: int
    data_reserva: datetime
    numero_pessoas: int

    class Config:
        orm_mode = True
