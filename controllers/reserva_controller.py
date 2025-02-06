from fastapi import APIRouter, HTTPException
from services.reserva_service import fetch_reservas, fetch_reserva_by_id, add_reserva, update_reserva_service, delete_reserva_service
from schemas.reserva_schema import ReservaCreate

router = APIRouter()

@router.get("/")
def get_reservas():
    return fetch_reservas()

@router.get("/{reserva_id}")
def get_reserva(reserva_id: int):
    reserva = fetch_reserva_by_id(reserva_id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reserva

@router.post("/")
def create_reserva(reserva: ReservaCreate):
    return add_reserva(reserva.dict())

@router.put("/{reserva_id}")
def update_reserva(reserva_id: int, reserva: ReservaCreate):
    updated_reserva = update_reserva_service(reserva_id, reserva.dict())
    if not updated_reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return updated_reserva

@router.delete("/{reserva_id}")
def delete_reserva(reserva_id: int):
    sucesso = delete_reserva_service(reserva_id)
    if sucesso:
        return {"message": "Reserva deletada com sucesso!"}
    raise HTTPException(status_code=404, detail="Reserva não encontrada")
