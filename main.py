from infrastructure.persistence.txt_livro_repository import (
    TxtLivroRepository,
)
from application.use_cases.livraria_service import LivrariaService
from presentation.view import LivrariaView
from presentation.controller import LivrariaController


def main():
    repository = TxtLivroRepository()
    service = LivrariaService(repository)
    view = LivrariaView()

    controller = LivrariaController(service, view)
    controller.executar()


if __name__ == "__main__":
    main()