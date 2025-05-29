class Multa:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Multa: R${self.valor:.2f}"
