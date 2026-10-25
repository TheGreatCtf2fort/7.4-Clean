import csv
from pathlib import Path

from domain.livro import Livro
from application.ports.livro_repository import LivroRepository


class TxtLivroRepository(LivroRepository):
    CAMPOS = ["id", "titulo", "autor", "preco", "estoque"]

    def __init__(self, caminho=None):
        raiz = Path(__file__).resolve().parents[2]
        self.caminho = Path(
            caminho or raiz / "data" / "livros.txt"
        )
        self.caminho.parent.mkdir(parents=True, exist_ok=True)

        if not self.caminho.exists():
            self._salvar_todos([])

    def _ler_todos(self) -> list[Livro]:
        with self.caminho.open(
            "r", encoding="utf-8", newline=""
        ) as arquivo:
            leitor = csv.DictReader(arquivo, delimiter="\t")
            return [
                Livro(
                    id=int(linha["id"]),
                    titulo=linha["titulo"],
                    autor=linha["autor"],
                    preco=float(linha["preco"]),
                    estoque=int(linha["estoque"]),
                )
                for linha in leitor
            ]

    def _salvar_todos(self, livros: list[Livro]) -> None:
        temporario = self.caminho.with_suffix(".tmp")

        with temporario.open(
            "w", encoding="utf-8", newline=""
        ) as arquivo:
            escritor = csv.DictWriter(
                arquivo,
                fieldnames=self.CAMPOS,
                delimiter="\t",
            )
            escritor.writeheader()

            for livro in livros:
                escritor.writerow({
                    "id": livro.id,
                    "titulo": livro.titulo,
                    "autor": livro.autor,
                    "preco": livro.preco,
                    "estoque": livro.estoque,
                })

        temporario.replace(self.caminho)

    def listar(self) -> list[Livro]:
        return self._ler_todos()

    def buscar_por_id(self, livro_id: int) -> Livro | None:
        return next(
            (
                livro for livro in self._ler_todos()
                if livro.id == livro_id
            ),
            None,
        )

    def adicionar(self, livro: Livro) -> None:
        livros = self._ler_todos()

        if any(item.id == livro.id for item in livros):
            raise ValueError("Já existe um livro com esse ID.")

        livros.append(livro)
        self._salvar_todos(livros)

    def atualizar(self, livro: Livro) -> None:
        livros = self._ler_todos()

        for indice, existente in enumerate(livros):
            if existente.id == livro.id:
                livros[indice] = livro
                self._salvar_todos(livros)
                return

        raise ValueError("Livro não encontrado.")

    def remover(self, livro_id: int) -> bool:
        livros = self._ler_todos()
        restantes = [
            livro for livro in livros
            if livro.id != livro_id
        ]

        if len(restantes) == len(livros):
            return False

        self._salvar_todos(restantes)
        return True