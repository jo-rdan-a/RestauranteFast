from typing import List, Optional
from datetime import datetime
import json
from models.reserva import Reserva

RESERVAS_FILE = 'data/reservas.json'

# Carregar reservas do arquivo JSON
def load_reservas() -> List[dict]:
    try:
        with open(RESERVAS_FILE, 'r') as file:
            data = json.load(file)
            for reserva in data:
                # Converte a string ISO 8601 para datetime
                if 'data' in reserva and isinstance(reserva['data'], str):
                    reserva['data'] = datetime.fromisoformat(reserva['data'])
            return data
    except FileNotFoundError:
        return []

# Salvar as reservas no arquivo JSON
def save_reservas(reservas: List[dict]):
    # Converte a data de datetime para string antes de salvar
    for reserva in reservas:
        reserva['data'] = reserva['data'].strftime('%Y-%m-%d')
    
    with open(RESERVAS_FILE, 'w') as file:
        json.dump(reservas, file, indent=4)

# Buscar todas as reservas
def fetch_reservas() -> List[dict]:
    return load_reservas()

# Buscar uma reserva específica pelo ID
def fetch_reserva_by_id(reserva_id: int) -> Optional[dict]:
    reservas = load_reservas()
    for reserva in reservas:
        if reserva['id'] == reserva_id:
            return reserva
    return None

# Criar uma nova reserva
def add_reserva(reserva_data: dict) -> dict:
    reservas = load_reservas()
    new_reserva = {
        "id": len(reservas) + 1,
        "mesa_id": reserva_data['mesa_id'],
        "data": reserva_data['data'].strftime('%Y-%m-%d'),  # Converte a data para string
        "nome_cliente": reserva_data['nome_cliente'],
        "numero_pessoas": reserva_data['numero_pessoas']
    }
    reservas.append(new_reserva)
    save_reservas(reservas)
    return new_reserva

# Atualizar uma reserva existente
def update_reserva_service(reserva_id: int, updated_data: dict) -> Optional[dict]:
    reservas = load_reservas()
    for reserva in reservas:
        if reserva['id'] == reserva_id:
            reserva.update(updated_data)
            save_reservas(reservas)
            return reserva
    return None

# Deletar uma reserva
def delete_reserva_service(reserva_id: int) -> bool:
    reservas = load_reservas()
    reservas_filtradas = [reserva for reserva in reservas if reserva["id"] != reserva_id]

    if len(reservas) == len(reservas_filtradas):
        return False  # Reserva não encontrada

    save_reservas(reservas_filtradas)
    return True  # Sucesso ao deletar
