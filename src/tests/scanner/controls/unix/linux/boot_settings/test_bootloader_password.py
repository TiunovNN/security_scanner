from scanner.controls.types import ControlStatus
from scanner.controls.unix.linux.boot_settings import bootloader_password
from tests.scanner.controls.conftest import BaseUnixControlTest


class TestBootloaderPassword(BaseUnixControlTest):
    origin = bootloader_password
    case_list = [
        (
            (
                '',
                '',
                '',
                '',
                '',
                '''
                #
                # DO NOT EDIT THIS FILE
                #
                # It is automatically generated by grub2-mkconfig using templates
                # from /etc/grub.d and settings from /etc/default/grub
                #

                ### BEGIN /etc/grub.d/00_header ###
                set pager=1

                if [ -s $prefix/grubenv ]; then
                  load_env
                fi
                if [ "${next_entry}" ] ; then
                   set default="${next_entry}"
                   set next_entry=
                   save_env next_entry
                   set boot_once=true
                else
                   set default="${saved_entry}"
                fi

                if [ x"${feature_menuentry_id}" = xy ]; then
                  menuentry_id_option="--id"
                else
                  menuentry_id_option=""
                fi

                export menuentry_id_option

                if [ "${prev_saved_entry}" ]; then
                  set saved_entry="${prev_saved_entry}"
                  save_env saved_entry
                  set prev_saved_entry=
                  save_env prev_saved_entry
                  set boot_once=true
                fi

                function savedefault {
                  if [ -z "${boot_once}" ]; then
                    saved_entry="${chosen}"
                    save_env saved_entry
                  fi
                }

                function load_video {
                  if [ x$feature_all_video_module = xy ]; then
                    insmod all_video
                  else
                    insmod efi_gop
                    insmod efi_uga
                    insmod ieee1275_fb
                    insmod vbe
                    insmod vga
                    insmod video_bochs
                    insmod video_cirrus
                  fi
                }

                terminal_output console
                if [ x$feature_timeout_style = xy ] ; then
                  set timeout_style=menu
                  set timeout=5
                # Fallback normal timeout code in case the timeout_style feature is
                # unavailable.
                else
                  set timeout=5
                fi
                ### END /etc/grub.d/00_header ###

                ### BEGIN /etc/grub.d/00_tuned ###
                set tuned_params=""
                set tuned_initrd=""
                ### END /etc/grub.d/00_tuned ###

                ### BEGIN /etc/grub.d/01_users ###
                if [ -f ${prefix}/user.cfg ]; then
                  source ${prefix}/user.cfg
                  if [ -n "${GRUB2_PASSWORD}" ]; then
                    set superusers="root"
                    export superusers
                    password_pbkdf2 root ${GRUB2_PASSWORD}
                  fi
                fi
                ### END /etc/grub.d/01_users ###

                ### BEGIN /etc/grub.d/10_linux ###
                menuentry 'CentOS Linux (3.10.0-862.6.3.el7.x86_64) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-693.el7.x86_64-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    set gfxpayload=keep
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-3.10.0-862.6.3.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet LANG=ru_RU.UTF-8
                    initrd16 /initramfs-3.10.0-862.6.3.el7.x86_64.img
                }
                menuentry 'CentOS Linux (3.10.0-693.21.1.el7.x86_64) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-693.el7.x86_64-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    set gfxpayload=keep
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-3.10.0-693.21.1.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet LANG=ru_RU.UTF-8
                    initrd16 /initramfs-3.10.0-693.21.1.el7.x86_64.img
                }
                menuentry 'CentOS Linux (3.10.0-693.el7.x86_64) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-693.el7.x86_64-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    set gfxpayload=keep
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-3.10.0-693.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet LANG=ru_RU.UTF-8
                    initrd16 /initramfs-3.10.0-693.el7.x86_64.img
                }
                menuentry 'CentOS Linux (0-rescue-7bce3c0e4bf04f6194ad919300b05bd4) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-0-rescue-7bce3c0e4bf04f6194ad919300b05bd4-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-0-rescue-7bce3c0e4bf04f6194ad919300b05bd4 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet
                    initrd16 /initramfs-0-rescue-7bce3c0e4bf04f6194ad919300b05bd4.img
                }

                ### END /etc/grub.d/10_linux ###

                ### BEGIN /etc/grub.d/20_linux_xen ###
                ### END /etc/grub.d/20_linux_xen ###

                ### BEGIN /etc/grub.d/20_ppc_terminfo ###
                ### END /etc/grub.d/20_ppc_terminfo ###

                ### BEGIN /etc/grub.d/30_os-prober ###
                ### END /etc/grub.d/30_os-prober ###

                ### BEGIN /etc/grub.d/40_custom ###
                # This file provides an easy way to add custom menu entries.  Simply type the
                # menu entries you want to add after this comment.  Be careful not to change
                # the 'exec tail' line above.
                ### END /etc/grub.d/40_custom ###

                ### BEGIN /etc/grub.d/41_custom ###
                if [ -f  ${config_directory}/custom.cfg ]; then
                  source ${config_directory}/custom.cfg
                elif [ -z "${config_directory}" -a -f  $prefix/custom.cfg ]; then
                  source $prefix/custom.cfg;
                fi
                ### END /etc/grub.d/41_custom ###
                ''',
                '',
            ),
            ControlStatus.Compliance,
            '''
            /boot/grub2/grub.conf:81:set superusers="root"
            /boot/grub2/grub.conf:83:password_pbkdf2 root ${GRUB2_PASSWORD}
            '''
        ),
        (
            (
                '',
                '',
                '',
                '',
                '',
                '''
                #
                # DO NOT EDIT THIS FILE
                #
                # It is automatically generated by grub2-mkconfig using templates
                # from /etc/grub.d and settings from /etc/default/grub
                #

                ### BEGIN /etc/grub.d/00_header ###
                set pager=1

                if [ -s $prefix/grubenv ]; then
                  load_env
                fi
                if [ "${next_entry}" ] ; then
                   set default="${next_entry}"
                   set next_entry=
                   save_env next_entry
                   set boot_once=true
                else
                   set default="${saved_entry}"
                fi

                if [ x"${feature_menuentry_id}" = xy ]; then
                  menuentry_id_option="--id"
                else
                  menuentry_id_option=""
                fi

                export menuentry_id_option

                if [ "${prev_saved_entry}" ]; then
                  set saved_entry="${prev_saved_entry}"
                  save_env saved_entry
                  set prev_saved_entry=
                  save_env prev_saved_entry
                  set boot_once=true
                fi

                function savedefault {
                  if [ -z "${boot_once}" ]; then
                    saved_entry="${chosen}"
                    save_env saved_entry
                  fi
                }

                function load_video {
                  if [ x$feature_all_video_module = xy ]; then
                    insmod all_video
                  else
                    insmod efi_gop
                    insmod efi_uga
                    insmod ieee1275_fb
                    insmod vbe
                    insmod vga
                    insmod video_bochs
                    insmod video_cirrus
                  fi
                }

                terminal_output console
                if [ x$feature_timeout_style = xy ] ; then
                  set timeout_style=menu
                  set timeout=5
                # Fallback normal timeout code in case the timeout_style feature is
                # unavailable.
                else
                  set timeout=5
                fi
                ### END /etc/grub.d/00_header ###

                ### BEGIN /etc/grub.d/00_tuned ###
                set tuned_params=""
                set tuned_initrd=""
                ### END /etc/grub.d/00_tuned ###

                ### BEGIN /etc/grub.d/01_users ###
                if [ -f ${prefix}/user.cfg ]; then
                  source ${prefix}/user.cfg
                fi
                ### END /etc/grub.d/01_users ###

                ### BEGIN /etc/grub.d/10_linux ###
                menuentry 'CentOS Linux (3.10.0-862.6.3.el7.x86_64) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-693.el7.x86_64-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    set gfxpayload=keep
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-3.10.0-862.6.3.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet LANG=ru_RU.UTF-8
                    initrd16 /initramfs-3.10.0-862.6.3.el7.x86_64.img
                }
                menuentry 'CentOS Linux (3.10.0-693.21.1.el7.x86_64) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-693.el7.x86_64-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    set gfxpayload=keep
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-3.10.0-693.21.1.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet LANG=ru_RU.UTF-8
                    initrd16 /initramfs-3.10.0-693.21.1.el7.x86_64.img
                }
                menuentry 'CentOS Linux (3.10.0-693.el7.x86_64) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-693.el7.x86_64-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    set gfxpayload=keep
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-3.10.0-693.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet LANG=ru_RU.UTF-8
                    initrd16 /initramfs-3.10.0-693.el7.x86_64.img
                }
                menuentry 'CentOS Linux (0-rescue-7bce3c0e4bf04f6194ad919300b05bd4) 7 (Core)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-0-rescue-7bce3c0e4bf04f6194ad919300b05bd4-advanced-9ea5b21c-0707-4cb0-b815-0cceb84c42c5' {
                    load_video
                    insmod gzio
                    insmod part_msdos
                    insmod xfs
                    set root='hd0,msdos1'
                    if [ x$feature_platform_search_hint = xy ]; then
                      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  74d1facc-c31b-4146-bd5e-dd78923689e6
                    else
                      search --no-floppy --fs-uuid --set=root 74d1facc-c31b-4146-bd5e-dd78923689e6
                    fi
                    linux16 /vmlinuz-0-rescue-7bce3c0e4bf04f6194ad919300b05bd4 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet
                    initrd16 /initramfs-0-rescue-7bce3c0e4bf04f6194ad919300b05bd4.img
                }

                ### END /etc/grub.d/10_linux ###

                ### BEGIN /etc/grub.d/20_linux_xen ###
                ### END /etc/grub.d/20_linux_xen ###

                ### BEGIN /etc/grub.d/20_ppc_terminfo ###
                ### END /etc/grub.d/20_ppc_terminfo ###

                ### BEGIN /etc/grub.d/30_os-prober ###
                ### END /etc/grub.d/30_os-prober ###

                ### BEGIN /etc/grub.d/40_custom ###
                # This file provides an easy way to add custom menu entries.  Simply type the
                # menu entries you want to add after this comment.  Be careful not to change
                # the 'exec tail' line above.
                ### END /etc/grub.d/40_custom ###

                ### BEGIN /etc/grub.d/41_custom ###
                if [ -f  ${config_directory}/custom.cfg ]; then
                  source ${config_directory}/custom.cfg
                elif [ -z "${config_directory}" -a -f  $prefix/custom.cfg ]; then
                  source $prefix/custom.cfg;
                fi
                ### END /etc/grub.d/41_custom ###
                ''',
                '',
            ),
            ControlStatus.NotCompliance,
            '''
            The password is not set up
            '''
        ),
    ]
