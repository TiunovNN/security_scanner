from scanner.transports import get_transport, exceptions
from scanner.mappings import unameOS
from scanner.const import OS

from scanner.types import BaseDetector
from .unix import detectors


class UnixDetector(BaseDetector):
    requisites = None
    detection_os = OS.UNIX
    detectors = detectors

    def detect(self):
        transport = get_transport('unix')
        result = transport.send_command('uname -s')

        if result.ExitStatus != 0:
            return False

        if result.Output and unameOS(result.Output) is not None:
            return True

        return False