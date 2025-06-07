from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from src.netman.core.devices.base_net_device import BaseNetDevice

class Switch(BaseNetDevice, ABC):
    def __init__(self, hostname: str | IPv4Address, protocol = None):
        super().__init__(hostname, protocol)
        self.name = None
        self.l2_interfaces = None

    @abstractmethod
    def _fetch_l2_interfaces(self):
        pass

    @abstractmethod
    def _fetch_name(self):
        pass

    @property
    def layer2_interfaces(self):
        if self.l2_interfaces is None:
            self.l2_interfaces = self._fetch_l2_interfaces()
        return self.l2_interfaces