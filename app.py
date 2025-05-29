import tkinter as tk
from tkinter import messagebox
from package.biblioteca import Biblioteca

biblioteca = Biblioteca()
biblioteca.carregar_dados()

def cadastrar_usuario():
    nome = entry_nome.get()
    tipo = tipo_var.get()
    if tipo == "aluno":
        biblioteca.cadastrar_aluno(nome)
        messagebox.showinfo("Sucesso", f"Aluno '{nome}' cadastrado.")
    elif tipo == "professor":
        biblioteca.cadastrar_professor(nome)
        messagebox.showinfo("Sucesso", f"Professor '{nome}' cadastrado.")
    else:
        messagebox.showwarning("Erro", "Selecione um tipo de usuário.")

def cadastrar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    biblioteca.cadastrar_livro(titulo, autor)
    messagebox.showinfo("Sucesso", f"Livro '{titulo}' cadastrado.")

def emprestar_livro():
    nome = entry_nome_emprestimo.get()
    titulo = entry_titulo_emprestimo.get()
    biblioteca.emprestar_livro(nome, titulo)

def devolver_livro():
    nome = entry_nome_devolucao.get()
    titulo = entry_titulo_devolucao.get()
    biblioteca.devolver_livro(nome, titulo)

def ver_multa():
    nome = entry_nome_multa.get()
    biblioteca.ver_multa(nome)

def salvar_sair():
    biblioteca.salvar_dados()
    root.destroy()

root = tk.Tk()
root.title("Sistema de Biblioteca")
root.geometry("500x600")

tk.Label(root, text="Cadastro de Usuário").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()
tipo_var = tk.StringVar()
tk.Radiobutton(root, text="Aluno", variable=tipo_var, value="aluno").pack()
tk.Radiobutton(root, text="Professor", variable=tipo_var, value="professor").pack()
tk.Button(root, text="Cadastrar Usuário", command=cadastrar_usuario).pack(pady=5)

tk.Label(root, text="Cadastro de Livro").pack()
entry_titulo = tk.Entry(root)
entry_titulo.pack()
entry_autor = tk.Entry(root)
entry_autor.pack()
tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro).pack(pady=5)

tk.Label(root, text="Empréstimo de Livro").pack()
entry_nome_emprestimo = tk.Entry(root)
entry_nome_emprestimo.pack()
entry_titulo_emprestimo = tk.Entry(root)
entry_titulo_emprestimo.pack()
tk.Button(root, text="Emprestar Livro", command=emprestar_livro).pack(pady=5)

tk.Label(root, text="Devolução de Livro").pack()
entry_nome_devolucao = tk.Entry(root)
entry_nome_devolucao.pack()
entry_titulo_devolucao = tk.Entry(root)
entry_titulo_devolucao.pack()
tk.Button(root, text="Devolver Livro", command=devolver_livro).pack(pady=5)

tk.Label(root, text="Consultar Multa do Usuário").pack()
entry_nome_multa = tk.Entry(root)
entry_nome_multa.pack()
tk.Button(root, text="Ver Multa", command=ver_multa).pack(pady=5)

tk.Button(root, text="Salvar e Sair", command=salvar_sair).pack(pady=10)
root.mainloop()
