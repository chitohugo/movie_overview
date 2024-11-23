from requests import Session

from app.utils import RequestAbstract


class RequestService(RequestAbstract):
    def __init__(self, token: str, session: Session) -> None:
        self.token = token
        self._session = session

    def get(self, url: str):
        headers = self.set_headers()

        return self._session.get(
            url,
            headers=headers
        )

    def set_headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
