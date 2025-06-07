from src.netman.core.devices.switch import Switch
from src.netman.core.enums.management_protocol import ManagementProtocol as MP
from src.netman.core.enums.cisco_devices import Cisco
from ipaddress import IPv4Address


class CiscoSwitch(Switch):
    def __init__(self, hostname: str | IPv4Address, device_type: Cisco, protocol: MP = None):
        self._device_type = device_type
        super().__init__(hostname, protocol)

    def get_config(self):
        return super().get_config()
    
    def _fetch_l2_interfaces(self):
        return super()._fetch_l2_interfaces()
    
    def _fetch_l3_interfaces(self):
        return super()._fetch_l3_interfaces()
    
    def _fetch_name(self):
        return super()._fetch_name()
    
    @property
    def device_type(self):
        return self._device_type
    
    @device_type.setter
    def device_type(self, device_type: Cisco):
        if not isinstance(device_type, Cisco):
            raise ValueError("device_type must be Cisco")
        self._device_type = device_type
    
if __name__ == "__main__":
    switch = CiscoSwitch("192.168.10.1", Cisco.IOSXE)
    print(switch.hostname)
    print(switch.device_type)