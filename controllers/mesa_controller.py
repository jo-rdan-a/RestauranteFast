from fastapi import APIRouter, HTTPException
from services.mesa_service import fetch_mesas, fetch_mesa_by_id, add_mesa, update_mesa_service, delete_mesa_service
from schemas.mesa_schema import MesaCreate

router = APIRouter()

@router.get("/")
def get_mesas():
    return fetch_mesas()

@router.get("/{mesa_id}")
def get_mesa(mesa_id: int):
    mesa = fetch_mesa_by_id(mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa não encontrada")
    return mesa

@router.post("/")
def create_mesa(mesa: MesaCreate):
    return add_mesa(mesa.dict())

@router.put("/{mesa_id}")
def update_mesa(mesa_id: int, mesa: MesaCreate):
    updated_mesa = update_mesa_service(mesa_id, mesa.dict())
    if not updated_mesa:
        raise HTTPException(status_code=404, detail="Mesa não encontrada")
    return updated_mesa

@router.delete("/{mesa_id}")
def delete_mesa(mesa_id: int):
    sucesso = delete_mesa_service(mesa_id)
    if sucesso:
        return {"message": "Mesa deletada com sucesso!"}
    raise HTTPException(status_code=404, detail="Mesa não encontrada")