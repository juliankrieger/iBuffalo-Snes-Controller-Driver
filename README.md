# iBuffalo-Snes-Controller-Driver
Linux drivers for the iBuffalo Snes controller

Snes controller Hardware Adress can be found at /dev/hidraw0
 	
Device Information can be found with "udevadm info -a -p $(udevadm info -q path -n /dev/hidraw0)" which produces following output:
	
	looking at device '/devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.0/0003:0583:2060.0006/hidraw/hidraw0':
    KERNEL=="hidraw0"
    SUBSYSTEM=="hidraw"
    DRIVER==""

	  looking at parent device '/devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.0/0003:0583:2060.0006':
	    KERNELS=="0003:0583:2060.0006"
	    SUBSYSTEMS=="hid"
	    DRIVERS=="hid-generic"
	    ATTRS{country}=="21"

	  looking at parent device '/devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.0':
	    KERNELS=="1-2:1.0"
	    SUBSYSTEMS=="usb"
	    DRIVERS=="usbhid"
	    ATTRS{authorized}=="1"
	    ATTRS{bAlternateSetting}==" 0"
	    ATTRS{bInterfaceClass}=="03"
	    ATTRS{bInterfaceNumber}=="00"
	    ATTRS{bInterfaceProtocol}=="00"
	    ATTRS{bInterfaceSubClass}=="00"
	    ATTRS{bNumEndpoints}=="01"
	    ATTRS{supports_autosuspend}=="1"

	  looking at parent device '/devices/pci0000:00/0000:00:14.0/usb1/1-2':
	    KERNELS=="1-2"
	    SUBSYSTEMS=="usb"
	    DRIVERS=="usb"
	    ATTRS{authorized}=="1"
	    ATTRS{avoid_reset_quirk}=="0"
	    ATTRS{bConfigurationValue}=="1"
	    ATTRS{bDeviceClass}=="00"
	    ATTRS{bDeviceProtocol}=="00"
	    ATTRS{bDeviceSubClass}=="00"
	    ATTRS{bMaxPacketSize0}=="8"
	    ATTRS{bMaxPower}=="100mA"
	    ATTRS{bNumConfigurations}=="1"
	    ATTRS{bNumInterfaces}==" 1"
	    ATTRS{bcdDevice}=="0100"
	    ATTRS{bmAttributes}=="80"
	    ATTRS{busnum}=="1"
	    ATTRS{configuration}==""
	    ATTRS{devnum}=="11"
	    ATTRS{devpath}=="2"
	    ATTRS{devspec}=="          (null)"
	    ATTRS{idProduct}=="2060"
	    ATTRS{idVendor}=="0583"
	    ATTRS{ltm_capable}=="no"
	    ATTRS{maxchild}=="0"
	    ATTRS{product}=="USB,2-axis 8-button gamepad  "
	    ATTRS{quirks}=="0x0"
	    ATTRS{removable}=="removable"
	    ATTRS{speed}=="1.5"
	    ATTRS{urbnum}=="43"
	    ATTRS{version}==" 1.10"

	  looking at parent device '/devices/pci0000:00/0000:00:14.0/usb1':
	    KERNELS=="usb1"
	    SUBSYSTEMS=="usb"
	    DRIVERS=="usb"
	    ATTRS{authorized}=="1"
	    ATTRS{authorized_default}=="1"
	    ATTRS{avoid_reset_quirk}=="0"
	    ATTRS{bConfigurationValue}=="1"
	    ATTRS{bDeviceClass}=="09"
	    ATTRS{bDeviceProtocol}=="01"
	    ATTRS{bDeviceSubClass}=="00"
	    ATTRS{bMaxPacketSize0}=="64"
	    ATTRS{bMaxPower}=="0mA"
	    ATTRS{bNumConfigurations}=="1"
	    ATTRS{bNumInterfaces}==" 1"
	    ATTRS{bcdDevice}=="0417"
	    ATTRS{bmAttributes}=="e0"
	    ATTRS{busnum}=="1"
	    ATTRS{configuration}==""
	    ATTRS{devnum}=="1"
	    ATTRS{devpath}=="0"
	    ATTRS{devspec}=="          (null)"
	    ATTRS{idProduct}=="0002"
	    ATTRS{idVendor}=="1d6b"
	    ATTRS{interface_authorized_default}=="1"
	    ATTRS{ltm_capable}=="no"
	    ATTRS{manufacturer}=="Linux 4.17.14-arch1-1-ARCH xhci-hcd"
	    ATTRS{maxchild}=="12"
	    ATTRS{product}=="xHCI Host Controller"
	    ATTRS{quirks}=="0x0"
	    ATTRS{removable}=="unknown"
	    ATTRS{serial}=="0000:00:14.0"
	    ATTRS{speed}=="480"
	    ATTRS{urbnum}=="9254"
	    ATTRS{version}==" 2.00"

	  looking at parent device '/devices/pci0000:00/0000:00:14.0':
	    KERNELS=="0000:00:14.0"
	    SUBSYSTEMS=="pci"
	    DRIVERS=="xhci_hcd"
	    ATTRS{ari_enabled}=="0"
	    ATTRS{broken_parity_status}=="0"
	    ATTRS{class}=="0x0c0330"
	    ATTRS{consistent_dma_mask_bits}=="64"
	    ATTRS{d3cold_allowed}=="1"
	    ATTRS{device}=="0x9d2f"
	    ATTRS{devspec}==""
	    ATTRS{dma_mask_bits}=="64"
	    ATTRS{driver_override}=="(null)"
	    ATTRS{enable}=="1"
	    ATTRS{irq}=="122"
	    ATTRS{local_cpulist}=="0-3"
	    ATTRS{local_cpus}=="f"
	    ATTRS{msi_bus}=="1"
	    ATTRS{numa_node}=="-1"
	    ATTRS{revision}=="0x21"
	    ATTRS{subsystem_device}=="0x380c"
	    ATTRS{subsystem_vendor}=="0x17aa"
	    ATTRS{vendor}=="0x8086"

	  looking at parent device '/devices/pci0000:00':
	    KERNELS=="pci0000:00"
	    SUBSYSTEMS==""
	    DRIVERS==""

Device udev rules can be created at /etc/udev/rules.d and tested with:
    udevadm test $(udevadm info -q path -n /dev/hidraw0)
    
    The best values to grab (as in /etc/udev/rules.d/99-snes.rules) are:
    KERNEL=="hidraw[0-9]*", SUBSYSTEM=="hidraw", SUBSYSTEMS=="usb", ATTRS{idVendor}=="0583", ATTRS{idProduct}=="2060"
    
More Device info:
    - Final symlink for usb product is at /dev/snes-controller
    
    - Device event endpoint can be found at /dev/input/event/by-path/pci-0000:00:14.0-usb-0:2:1.0-event-joystick
    
        or at by-id/usb-0583_USB_2-axis_8-button_gamepad-event-joystick
        or at by-id/usb-0583_USB_2-axis_8-button_gamepad-gamepad-joystick
    
    And can be tested with "evtest /dev/input/event/by-path/pci-0000:00:14.0-usb-0:2:1.0-event-joystick"
    
    - Device syspoint is at /sys/bus/usb/devices/1-2


