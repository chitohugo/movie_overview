import sys

from dependency_injector.wiring import Provide, inject

from app.containers import Container
from app.services.llm_service import LLMService
from app.services.movie_service import MovieService


@inject
def main(
        movie_service: MovieService = Provide[Container.movie_service],
        llm_service: LLMService = Provide[Container.llm_service]
) -> None:
    title = "titanic"
    results = movie_service.get_movie(title)
    llm_service.invoke(results)


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main(*sys.argv[1:])