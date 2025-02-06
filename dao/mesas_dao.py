import json
from models.mesa import Mesa

MESAS_FILE = 'data/mesas.json'

def load_mesas():
    try:
        with open('data/mesas.json', 'r', encoding='utf-8') as file:  # 🔹 Definir encoding='utf-8'
            return json.load(file)
    except FileNotFoundError:
        return []

def save_mesas(mesas):
    with open(MESAS_FILE, 'w') as file:
        json.dump([mesa.to_dict() for mesa in mesas], file, indent=4)

def get_all_mesas():
    return load_mesas()

def add_mesa(mesa_data):
    mesas = load_mesas()
    new_mesa = Mesa(id=len(mesas) + 1, **mesa_data)
    mesas.append(new_mesa)
    save_mesas(mesas)
    return new_mesa
