import pickle, os
from package.usuario import Aluno, Professor
from package.livro import Livro
from package.emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def salvar_dados(self):
        with open("dados.pkl", "wb") as f:
            pickle.dump((self.usuarios, self.livros, self.emprestimos), f)

    def carregar_dados(self):
        if os.path.exists("dados.pkl"):
            with open("dados.pkl", "rb") as f:
                self.usuarios, self.livros, self.emprestimos = pickle.load(f)

    def buscar_usuario(self, nome):
        return next((u for u in self.usuarios if u.get_nome() == nome), None)

    def buscar_livro(self, titulo):
        return next((l for l in self.livros if l.get_titulo() == titulo), None)

    def cadastrar_aluno(self, nome):
        self.usuarios.append(Aluno(nome))

    def cadastrar_professor(self, nome):
        self.usuarios.append(Professor(nome))

    def cadastrar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))

    def emprestar_livro(self, nome_usuario, titulo_livro):
        usuario = self.buscar_usuario(nome_usuario)
        livro = self.buscar_livro(titulo_livro)
        if usuario and livro and livro.esta_disponivel():
            emprestimo = Emprestimo(usuario, livro)
            usuario.adicionar_emprestimo(emprestimo)
            self.emprestimos.append(emprestimo)
            usuario.notificar("Livro emprestado com sucesso!")
        else:
            print("Erro ao emprestar.")

    def devolver_livro(self, nome_usuario, titulo_livro):
        usuario = self.buscar_usuario(nome_usuario)
        for e in usuario.get_emprestimos():
            if e.livro.get_titulo() == titulo_livro and e.data_devolucao is None:
                e.devolver()
                usuario.notificar("Livro devolvido.")
                return
        print("Empréstimo não encontrado.")

    def ver_multa(self, nome_usuario):
        usuario = self.buscar_usuario(nome_usuario)
        if usuario:
            valor = usuario.calcular_multa()
            print(f"Multa atual: R$ {valor:.2f}")
