import abc
import logging
from enum import Enum
from typing import Union, List

from utility import AddLoggerMeta

logger = logging.getLogger(__name__)

_detected = set()


class ControlStatus(Enum):
    NotChecked = 0
    Compliance = 1
    NotCompliance = 2
    NotApplicable = 3
    Error = 4


class TransportMeta(AddLoggerMeta, abc.ABCMeta):
    pass


class BaseControlMeta(abc.ABCMeta, AddLoggerMeta):
    pass


class BaseDetectorMeta(abc.ABCMeta, AddLoggerMeta):
    pass


def os_detect(os: str) -> None:
    logger.info(f'OS: {os} has been detected')
    _detected.add(os)


def is_os_detect(os: str) -> bool:
    result = os in _detected
    logger.debug(f'Is_os_detected: {os} is {result}')
    return result


class BaseTransport(metaclass=TransportMeta):
    @abc.abstractmethod
    def connect(self) -> None:
        pass

    @property
    @abc.abstractmethod
    def is_connect(self) -> bool:
        pass


class BaseDetector(metaclass=BaseDetectorMeta):
    @property
    @abc.abstractmethod
    def requisites(self) -> Union[List[str], str]:
        pass

    @property
    @abc.abstractmethod
    def detection_os(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def detectors(self) -> List:
        pass

    @property
    def requirements(self) -> bool:
        if self.requisites:
            if isinstance(self.requisites, List):
                return all(map(is_os_detect, self.requisites))
            return is_os_detect(self.requisites)
        return True

    @abc.abstractmethod
    def detect(self) -> List:
        pass

    def run(self) -> List:
        if self.requirements and self.detect():
            os_detect(self.detection_os)
            return self.detectors
        return []

    def __repr__(self):
        return f'{self.__class__.__qualname__}()'


class ControlResult:
    def __init__(self, number: int):
        self.number = number
        self.result = None
        self.status = ControlStatus.NotChecked

    def not_applicable(self, reason: str) -> None:
        self.status = ControlStatus.NotApplicable
        self.result = reason

    def compliance(self, result: str) -> None:
        self.status = ControlStatus.Compliance
        self.result = result

    def not_compliance(self, result: str) -> None:
        self.status = ControlStatus.NotCompliance
        self.result = result

    def error(self, result: str) -> None:
        self.status = ControlStatus.Error
        self.result = result


class BaseContol(metaclass=BaseControlMeta):
    def __init__(self, number):
        self.control = ControlResult(number=number)

    @abc.abstractmethod
    def prerequisite(self) -> bool:
        pass

    @abc.abstractmethod
    def check(self) -> None:
        pass

    def run(self):
        if self.prerequisite():
            try:
                self.check()
            except RuntimeError as e:
                self.control.error(f'{e}')