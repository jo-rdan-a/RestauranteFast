import json
from models.reserva import Reserva
from datetime import datetime

RESERVAS_FILE = 'data/reservas.json'

def load_reservas():
    try:
        with open(RESERVAS_FILE, 'r') as file:
            data = json.load(file)
            for item in data:
                if 'data' in item and isinstance(item['data'], str):
                    item['data'] = datetime.fromisoformat(item['data'])
            return data
    except FileNotFoundError:
        return []

def save_reservas(data):
    def custom_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Tipo {type(obj)} não é serializável em JSON.")
    
    with open(RESERVAS_FILE, 'w') as file:
        json.dump(data, file, indent=4, default=custom_serializer)

def get_all_reservas():
    data = load_reservas()
    return [Reserva(**item) for item in data]

def get_reserva_by_id(reserva_id: int):
    data = load_reservas()
    for item in data:
        if item['id'] == reserva_id:
            return Reserva(**item)
    return None

def create_reserva(reserva_data):
    reservas = load_reservas()
    new_reserva = Reserva(**reserva_data)
    reservas.append(new_reserva.to_dict())
    save_reservas(reservas)
    return new_reserva

def add_reserva(reserva: dict):
    reservas = load_reservas()
    reserva['id'] = len(reservas) + 1
    reserva['data'] = reserva['data'].isoformat()
    reservas.append(reserva)
    save_reservas(reservas)
    return reserva

def update_reserva_dao(reserva_id: int, updated_data: dict):
    reservas = load_reservas()
    for index, reserva in enumerate(reservas):
        if reserva['id'] == reserva_id:
            reservas[index].update(updated_data)
            save_reservas(reservas)
            return reservas[index]
    return None

def delete_reserva(reserva_id: int):
    reservas = load_reservas()
    reservas = [reserva for reserva in reservas if reserva['id'] != reserva_id]
    save_reservas(reservas)
    return {"message": "Reserva deletada com sucesso"}
