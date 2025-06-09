from abc import ABC, abstractmethod
from ipaddress import IPv4Address

from src.netman.core.enums.management_protocol import ManagementProtocol as MP
from src.netman.core.managers.ssh_manager import SSHManager

class BaseNetDevice(ABC):
    def __init__(self, hostname: str | IPv4Address, protocol: MP = None):
        self.hostname = hostname
        if protocol:
            self.set_manager(protocol)
        else:
            self.manager = None

    def set_manager(self, protocol: MP):
        if protocol == MP.SSH:
            # use SSHManager
            self.manager = SSHManager(self.hostname)
            raise ValueError("Not yet implemeneted.")
        elif protocol == MP.RESTCONF:
            # use RESTCONFManager
            raise ValueError("Not yet implemeneted.")
        elif protocol == MP.NETCONF:
            # use NETCONFManager
            raise ValueError("Not yet implemeneted.")
        else:
            raise ValueError("Manager protocol must be of type ManagementProtocol.")
        
    
    @abstractmethod
    def get_config(self):
        pass
        