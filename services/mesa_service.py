from dao.mesas_dao import load_mesas, save_mesas
from models.mesa import Mesa

def fetch_mesas():
    """Retorna todas as mesas disponíveis."""
    return load_mesas()

def fetch_mesa_by_id(mesa_id):
    """Retorna uma mesa específica pelo ID."""
    mesas = load_mesas()
    for mesa in mesas:
        if mesa["id"] == mesa_id:
            return mesa
    return None

def add_mesa(mesa_data):
    """Adiciona uma nova mesa."""
    mesas = load_mesas()
    novo_id = max((mesa["id"] for mesa in mesas), default=0) + 1

    nova_mesa = Mesa(id=novo_id, numero=mesa_data["numero"], lugares=mesa_data["lugares"])
    mesas.append(nova_mesa.to_dict())

    save_mesas(mesas)
    return nova_mesa.to_dict()

def update_mesa_service(mesa_id, mesa_data):
    """Atualiza uma mesa existente pelo ID."""
    mesas = load_mesas()
    for mesa in mesas:
        if mesa["id"] == mesa_id:
            mesa["numero"] = mesa_data["numero"]
            mesa["lugares"] = mesa_data["lugares"]
            save_mesas(mesas)
            return mesa
    return None

def delete_mesa_service(mesa_id):
    """Remove uma mesa pelo ID."""
    mesas = load_mesas()
    novas_mesas = [mesa for mesa in mesas if mesa["id"] != mesa_id]

    if len(novas_mesas) == len(mesas):
        return False  # Nenhuma mesa foi removida

    save_mesas(novas_mesas)
    return True
