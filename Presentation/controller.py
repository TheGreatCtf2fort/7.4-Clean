class LivrariaController:
    def __init__(self, service, view):
        self.service = service
        self.view = view

    def executar(self):
        while True:
            opcao = self.view.mostrar_menu()

            try:
                if opcao == "1":
                    titulo, autor, preco, estoque = (
                        self.view.solicitar_livro()
                    )
                    livro = self.service.cadastrar_livro(
                        titulo, autor, preco, estoque
                    )
                    self.view.mostrar_mensagem(
                        f"Livro cadastrado! ID: {livro.id}"
                    )

                elif opcao == "2":
                    self.view.mostrar_livros(
                        self.service.listar_livros()
                    )

                elif opcao == "3":
                    termo = self.view.solicitar_busca()
                    self.view.mostrar_livros(
                        self.service.buscar_livros(termo)
                    )

                elif opcao == "4":
                    livro_id = self.view.solicitar_id()
                    self.service.excluir_livro(livro_id)
                    self.view.mostrar_mensagem(
                        "Livro excluído com sucesso."
                    )

                elif opcao == "5":
                    livro_id = self.view.solicitar_id()
                    quantidade = self.view.solicitar_quantidade()
                    venda = self.service.vender_livro(
                        livro_id, quantidade
                    )
                    self.view.mostrar_mensagem(
                        f"Venda realizada!\n"
                        f"Livro: {venda['livro'].titulo}\n"
                        f"Total: R$ {venda['total']:.2f}\n"
                        f"Estoque restante: "
                        f"{venda['estoque_restante']}"
                    )

                elif opcao == "0":
                    self.view.mostrar_mensagem(
                        "Aplicativo encerrado."
                    )
                    break

                else:
                    self.view.mostrar_erro("Opção inválida.")

            except (ValueError, TypeError) as erro:
                self.view.mostrar_erro(str(erro))
            except OSError as erro:
                self.view.mostrar_erro(
                    f"Falha ao acessar os dados: {erro}"
                )