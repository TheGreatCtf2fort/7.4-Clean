from domain.livro import Livro
from application.ports.livro_repository import LivroRepository


class LivrariaService:
    def __init__(self, repository: LivroRepository):
        self.repository = repository

    def cadastrar_livro(
        self, titulo, autor, preco, estoque
    ) -> Livro:
        titulo = titulo.strip()
        autor = autor.strip()

        if not titulo or not autor:
            raise ValueError("Título e autor são obrigatórios.")

        ids = [livro.id for livro in self.repository.listar()]
        novo_id = max(ids, default=0) + 1

        livro = Livro(
            id=novo_id,
            titulo=titulo,
            autor=autor,
            preco=preco,
            estoque=estoque,
        )

        self.repository.adicionar(livro)
        return livro

    def listar_livros(self) -> list[Livro]:
        return self.repository.listar()

    def buscar_livros(self, termo: str) -> list[Livro]:
        termo = termo.strip().casefold()

        return [
            livro for livro in self.repository.listar()
            if termo in livro.titulo.casefold()
        ]

    def excluir_livro(self, livro_id: int) -> None:
        if not self.repository.remover(livro_id):
            raise ValueError("Livro não encontrado.")

    def vender_livro(self, livro_id: int, quantidade: int):
        livro = self.repository.buscar_por_id(livro_id)

        if livro is None:
            raise ValueError("Livro não encontrado.")

        total = livro.vender(quantidade)
        self.repository.atualizar(livro)

        return {
            "livro": livro,
            "quantidade": quantidade,
            "total": total,
            "estoque_restante": livro.estoque,
        }