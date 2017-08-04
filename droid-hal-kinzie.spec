# These and other macros are documented in dhd/droid-hal-device.inc

%define device kinzie
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto X Force

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.touch.sh\
/init.qcom.ssr.sh\
/selinux_version\
/service_contexts\
%{nil}

#%define makefstab_skip_entries /sys/fs/cgroup/bfqio /sys/fs/pstore none

%include rpm/dhd/droid-hal-device.inc