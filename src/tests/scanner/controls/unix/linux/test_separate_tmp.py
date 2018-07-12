from scanner.types import ControlStatus
from scanner.controls.unix.linux.tmp import separate_tmp
from tests.scanner.controls.conftest import BaseUnixTest


class TestCase(BaseUnixTest):
    origin = separate_tmp
    case_list = [
        (
            ''' 
            sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
            proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
            tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime)
            udev on /dev type devtmpfs (rw,nosuid,relatime,size=3995276k,nr_inodes=998819,mode=755)
            devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
            tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=805012k,mode=755)
            ''',
            ControlStatus.Compliance,
            '/tmp has been mounted on tmpfs'
        ),
        (
            ''' 
            sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
            proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
            udev on /dev type devtmpfs (rw,nosuid,relatime,size=3995276k,nr_inodes=998819,mode=755)
            devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
            tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime,size=805012k,mode=755)
            ''',
            ControlStatus.NotCompliance,
            '/tmp has not been mounted on separated partition'
        ),
    ]
