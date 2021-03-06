from abc import ABC, abstractmethod
from functools import partial
from textwrap import dedent

from scanner.types import ControlStatus


def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ != 'test_case':
        return metafunc

    idlist = [
        f'Test case {i+1}'
        for i in range(len(metafunc.cls.case_list))
    ]

    argnames = ['text', 'status', 'result']
    argvalues = []

    for text, status, result in metafunc.cls.case_list:
        if isinstance(text, str):
            text = (dedent(text),)
        else:
            text = tuple(dedent(item) for item in text)

        argvalues.append((text, status, result and dedent(result).strip()))

    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


class BaseUnixControlTest(ABC):
    @property
    @abstractmethod
    def case_list(self):
        pass

    @property
    @abstractmethod
    def origin(self):
        pass

    @staticmethod
    def not_passed_prerequisite():
        return False

    def test_case(self, monkeypatch, text, status, result, get_transport_patch):
        monkeypatch.setattr(
            self.origin,
            'get_transport',
            partial(get_transport_patch, text=text)
        )
        monkeypatch.setattr(
            self.origin.Control, 'prerequisite', lambda self_: True)
        control = self.origin.Control()
        control.run()
        assert control.control.status == status
        assert control.result == result

    def test_execute_not_checked(self, monkeypatch):
        control = self.origin.Control()
        monkeypatch.setattr(
            control, 'prerequisite', self.not_passed_prerequisite)
        control.run()
        assert control.control.status == ControlStatus.NotChecked
