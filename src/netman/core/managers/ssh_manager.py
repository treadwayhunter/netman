from src.netman.core.managers.base_manager import BaseManager
from src.netman.core.enums.base_device_type import BaseDeviceType
from src.netman.core.enums.cisco_devices import Cisco
from ipaddress import IPv4Address
from netmiko import ConnectHandler

# To make the best use of this Manager, SSH maintains a persistent
# connection. 

class SSHManager(BaseManager):
    def __init__(self, hostname: str | IPv4Address, device_type: BaseDeviceType):
        super().__init__(hostname)

    def get_config(self):
        pass

    def get_device_name(self):
        pass