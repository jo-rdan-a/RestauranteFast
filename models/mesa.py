class Mesa:
    def __init__(self, id: int, numero: int, capacidade: int):
        self.id = id
        self.numero = numero
        self.capacidade = capacidade

    def to_dict(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "capacidade": self.capacidade
        }
