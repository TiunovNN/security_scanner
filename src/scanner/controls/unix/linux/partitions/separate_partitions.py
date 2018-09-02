from scanner.const import os
from scanner.controls import BaseContol
from scanner.detect.types import is_item_detected
from scanner.functions.unix.mount_parser import MountFinditer


class Control(BaseContol, control_number=3):
    path_list = (
        '/var',
        '/var/tmp',
        '/var/log',
        '/var/log/audit',
        '/home',
        '/tmp'
    )

    def prerequisite(self):
        return is_item_detected(os.LINUX)

    def check(self):
        transport = self.get_transport('unix')
        result = transport.send_command('mount')

        separated = dict(
            (item.Path, item.Device)
            for item in MountFinditer(text=result.Output)
            if item.Path in self.path_list
        )

        missed_paths = [
            path
            for path in self.path_list
            if path not in separated
        ]

        results = []
        for path, device in sorted(separated.items()):
            results.append(f'{path} has been mounted on {device}')

        for path in sorted(missed_paths):
            results.append(f'{path} has not been mounted on separate partition')

        result = '\n'.join(results)

        if not missed_paths:
            self.control.compliance(result=result)
        else:
            self.control.not_compliance(result=result)
