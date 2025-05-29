from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
        self.prazo = self.data_emprestimo + timedelta(days=7)
        livro.emprestar()

    def devolver(self):
        self.data_devolucao = datetime.now()
        self.livro.devolver()

    def em_atraso(self):
        if self.data_devolucao is None:
            return datetime.now() > self.prazo
        return self.data_devolucao > self.prazo

    def dias_atraso(self):
        if self.em_atraso():
            data_final = self.data_devolucao or datetime.now()
            return (data_final - self.prazo).days
        return 0
