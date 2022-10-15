import storage
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "REV41"
storage.remount("/", readonly=True)
storage.enable_usb_drive()