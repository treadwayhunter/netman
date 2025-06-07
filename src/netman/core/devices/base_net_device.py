from abc import ABC, abstractmethod
from ipaddress import IPv4Address

from src.netman.core.enums.management_protocol import ManagementProtocol

class BaseNetDevice(ABC):
    def __init__(self, hostname: str | IPv4Address, protocol = None):
        self.hostname = hostname
        if protocol:
            self.set_manager(protocol)

    @abstractmethod
    def get_config(self):
        pass

    def set_manager(self, protocol: ManagementProtocol):
        if protocol == ManagementProtocol.SSH:
            # use SSHManager
            pass
        elif protocol == ManagementProtocol.RESTCONF:
            # use RESTCONFManager
            pass
        elif protocol == ManagementProtocol.NETCONF:
            # use NETCONFManager
            pass
        else:
            raise ValueError("Manager protocol must be of type ManagementProtocol.")
        