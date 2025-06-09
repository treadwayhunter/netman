from src.netman.core.enums.base_device_type import BaseDeviceType
from enum import auto

class Cisco(BaseDeviceType):
    IOSXE = auto()
    NXOS = auto()
    MERAKI = auto()

    @staticmethod
    def device_name_command(device_type, protocol):
        pass