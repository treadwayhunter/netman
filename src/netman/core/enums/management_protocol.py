from enum import Enum, auto

class ManagementProtocol(Enum):
    SSH = auto()
    NETCONF = auto()
    RESTCONF = auto()