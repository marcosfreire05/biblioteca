from package.notificacao import Notificacao

class Usuario(Notificacao):
    def __init__(self, nome):
        self._nome = nome
        self._emprestimos = []

    def get_nome(self):
        return self._nome

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def get_emprestimos(self):
        return self._emprestimos

    def calcular_multa(self):
        raise NotImplementedError

class Aluno(Usuario):
    def calcular_multa(self):
        return sum([e.dias_atraso() * 1.0 for e in self._emprestimos if e.em_atraso()])

class Professor(Usuario):
    def calcular_multa(self):
        return sum([e.dias_atraso() * 0.5 for e in self._emprestimos if e.em_atraso()])
