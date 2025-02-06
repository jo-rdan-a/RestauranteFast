from datetime import datetime

class Reserva:
    def __init__(self, id: int, mesa_id: int, data: datetime, hora: str, nome_responsavel: str):
        self.id = id
        self.mesa_id = mesa_id
        self.data = data
        self.hora = hora
        self.nome_responsavel = nome_responsavel

    def to_dict(self):
        return {
            "id": self.id,
            "mesa_id": self.mesa_id,
            "data": self.data.strftime('%Y-%m-%d'),
            "hora": self.hora,
            "nome_responsavel": self.nome_responsavel
        }