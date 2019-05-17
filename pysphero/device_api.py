import abc
from enum import Enum

from pysphero import core
from pysphero.packet import Packet


class DeviceId(Enum):
    api_processor = 0x10
    system_info = 0x11
    system_modes = 0x12
    power = 0x13
    driving = 0x16
    animatronics = 0x17
    sensors = 0x18
    user_io = 0x1a


class DeviceApiABC(abc.ABC):
    device_id: Enum = NotImplemented

    def __init__(self, sphero_core: core.SpheroCore):
        self.sphero_core = sphero_core

    def request(self, command_id: Enum, with_api_error: bool = True, timeout: int = 10, **kwargs) -> Packet:
        return self.sphero_core.request(
            self.packet(command_id=command_id.value, **kwargs),
            with_api_error=with_api_error,
            timeout=timeout,
        )

    def packet(self, **kwargs):
        packet = Packet(
            device_id=self.device_id.value,
            **kwargs
        )
        return packet