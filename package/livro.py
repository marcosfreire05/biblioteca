class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = True

    def get_titulo(self):
        return self._titulo

    def esta_disponivel(self):
        return self._disponivel

    def emprestar(self):
        self._disponivel = False

    def devolver(self):
        self._disponivel = True
