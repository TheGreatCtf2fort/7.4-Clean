from abc import ABC, abstractmethod
from domain.livro import Livro


class LivroRepository(ABC):

    @abstractmethod
    def listar(self) -> list[Livro]:
        pass

    @abstractmethod
    def buscar_por_id(self, livro_id: int) -> Livro | None:
        pass

    @abstractmethod
    def adicionar(self, livro: Livro) -> None:
        pass

    @abstractmethod
    def atualizar(self, livro: Livro) -> None:
        pass

    @abstractmethod
    def remover(self, livro_id: int) -> bool:
        pass