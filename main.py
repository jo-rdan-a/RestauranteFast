from fastapi import FastAPI, HTTPException
from controllers.mesa_controller import router as mesa_router
from controllers.reserva_controller import router as reserva_router

app = FastAPI(title="Sistema de Reservas", description="API para gerenciamento de reservas e mesas", version="1.0")

# Registrando os controllers na aplicação
app.include_router(mesa_router, prefix="/mesas", tags=["Mesas"])
app.include_router(reserva_router, prefix="/reservas", tags=["Reservas"])

@app.get("/")
def root():
    return {"message": "Bem-vindo ao Sistema de Reservas"}

