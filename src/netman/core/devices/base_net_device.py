from abc import ABC, abstractmethod
from ipaddress import IPv4Address

from src.netman.core.enums.management_protocol import ManagementProtocol as MP

class BaseNetDevice(ABC):
    def __init__(self, hostname: str | IPv4Address, protocol: MP = None):
        self.hostname = hostname
        if protocol:
            self.set_manager(protocol)
        else:
            self.manager = None

    @abstractmethod
    def get_config(self):
        pass

    def set_manager(self, protocol: MP):
        if protocol == MP.SSH:
            # use SSHManager
            pass
        elif protocol == MP.RESTCONF:
            # use RESTCONFManager
            pass
        elif protocol == MP.NETCONF:
            # use NETCONFManager
            pass
        else:
            raise ValueError("Manager protocol must be of type ManagementProtocol.")
        