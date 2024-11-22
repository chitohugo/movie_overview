from abc import ABC, abstractmethod


class RequestServiceAbstract(ABC):
    @abstractmethod
    def get(self, url: str):
        pass

    @abstractmethod
    def set_headers(self):
        pass
