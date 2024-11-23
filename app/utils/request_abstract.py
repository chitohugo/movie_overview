from abc import ABC, abstractmethod


class RequestAbstract(ABC):
    @abstractmethod
    def get(self, url: str):
        pass

    @abstractmethod
    def set_headers(self):
        pass
