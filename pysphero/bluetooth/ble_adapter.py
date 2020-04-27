import abc
from typing import Callable

from pysphero.bluetooth.packet_collector import PacketCollector
from pysphero.packet import Packet


class AbstractBleAdapter(abc.ABC):
    def __init__(self, mac_address):
        self.mac_address = mac_address
        self.packet_collector = PacketCollector()

    def close(self):
        ...

    def write(self, packet: Packet, *, timeout: float = 10, raise_api_error: bool = True) -> Packet:
        """
         Method allow send request packet and get response packet

         :param packet: request packet
         :param timeout: timeout waiting for a response from sphero
         :param raise_api_error: raise exception when receive api error
         :return Packet: response packet
         """

    def start_notify(self, packet: Packet, callback: Callable, timeout: float = 10):
        ...

    def stop_notify(self, packet: Packet):
        ...
