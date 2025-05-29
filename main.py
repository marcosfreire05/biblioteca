from package.biblioteca import Biblioteca

biblioteca = Biblioteca()

def menu():
    while True:
        print("\n--- Menu Biblioteca ---")
        print("1. Cadastrar usuário")
        print("2. Cadastrar livro")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Ver multas")
        print("6. Sair")
        op = input("Escolha: ")

        if op == '1':
            nome = input("Nome: ")
            tipo = input("Tipo (aluno/professor): ")
            if tipo.lower() == 'aluno':
                biblioteca.cadastrar_aluno(nome)
            else:
                biblioteca.cadastrar_professor(nome)
        elif op == '2':
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            biblioteca.cadastrar_livro(titulo, autor)
        elif op == '3':
            usuario = input("Nome do usuário: ")
            livro = input("Título do livro: ")
            biblioteca.emprestar_livro(usuario, livro)
        elif op == '4':
            usuario = input("Nome do usuário: ")
            livro = input("Título do livro: ")
            biblioteca.devolver_livro(usuario, livro)
        elif op == '5':
            usuario = input("Nome do usuário: ")
            biblioteca.ver_multa(usuario)
        elif op == '6':
            break
        else:
            print("Opção inválida")

menu()
