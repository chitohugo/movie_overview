from .base_service import BaseService
from .request_service import RequestService


class MovieService(BaseService):
    def __init__(
            self,
            service: RequestService
    ) -> None:
        self.service = service
        super().__init__()

    def get_movie(self, title: str) -> str:
        self.logger.info(f"Getting movie {title}")

        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"

        response = self.service.get(url)
        return response.text
