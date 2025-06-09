from src.netman.core.managers.base_manager import BaseManager
from ipaddress import IPv4Address
from netmiko import ConnectHandler

# To make the best use of this Manager, SSH maintains a persistent
# connection. 

class SSHManager(BaseManager):
    def __init__(self, hostname: str | IPv4Address, ):
        super().__init__(hostname)

    def get_config(self):
        pass