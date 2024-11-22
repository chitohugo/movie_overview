from app.services.base_service import BaseService
from app.services.movie_service import MovieService


class BotService(BaseService):
    def __init__(self, movie_service: MovieService) -> None:
        self.movie_service: movie_service
        super().__init__()

    def search_movie(self):
        pass
