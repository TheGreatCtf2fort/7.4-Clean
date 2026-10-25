class LivrariaView:
    def mostrar_menu(self):
        print("\n===== LIVRARIA CLEAN ARCHITECTURE =====")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro")
        print("4. Excluir livro")
        print("5. Vender livro")
        print("0. Sair")
        return input("Escolha: ").strip()

    def solicitar_livro(self):
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        preco = float(input("Preço (R$): ").replace(",", "."))
        estoque = int(input("Estoque inicial: "))
        return titulo, autor, preco, estoque

    def solicitar_id(self):
        return int(input("ID do livro: "))

    def solicitar_quantidade(self):
        return int(input("Quantidade para vender: "))

    def solicitar_busca(self):
        return input("Título para buscar: ").strip()

    def mostrar_livros(self, livros):
        if not livros:
            print("Nenhum livro encontrado.")
            return

        for livro in livros:
            print(
                f"ID: {livro.id} | {livro.titulo} | "
                f"Autor: {livro.autor} | "
                f"Preço: R$ {livro.preco:.2f} | "
                f"Estoque: {livro.estoque}"
            )

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_erro(self, mensagem):
        print(f"Erro: {mensagem}")