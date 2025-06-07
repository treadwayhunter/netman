from abc import ABC, abstractmethod
from ipaddress import IPv4Address

class BaseManager(ABC):
    def __init__(self, hostname: str | IPv4Address):
        self.hostname = hostname

    @abstractmethod
    def get_config(self):
        pass
