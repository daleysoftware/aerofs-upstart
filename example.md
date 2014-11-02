    root@ubuntu64:/home/vagrant# bash <(curl -sL https://bit.ly/10dm1z5)
    AeroFS Quick Installation Utility
    The easist, fastest way to install AeroFS on headless Ubuntu systems.

    Which AeroFS Service would you like to install?
    [0] AeroFS Team Server
    [1] AeroFS
    Enter a number [0, 1]: 0
    Selection 0 okay? [Y/n] Y

    Are you using AeroFS Private Cloud or Hybrid Cloud?
    [0] Private
    [1] Hybrid
    Enter a number [0, 1]: 0
    Selection 0 okay? [Y/n] Y

    Please enter the DNS hostname of your Appliance.
    PC Appliance DNS Host: share.syncfs.com
    PC Appliance DNS Host "share.syncfs.com" okay? [Y/n] Y

    Downloading and installing AeroFS...
    Downloaded 67056318 of 67056318 bytes (100.00%)
    Selecting previously unselected package aerofsts-installer-0.
    (Reading database ... 51349 files and directories currently installed.)
    Unpacking aerofsts-installer-0 (from .../share.syncfs.com-aerofsts-installer-0.141101.11242.deb) ...
    Setting up aerofsts-installer-0 (0.141101.11242) ...
    procps stop/waiting

    Creating aerofs user...

    Running AeroFS installation program...
    Press CTRL-C to stop the CLI when setup is finished.
    Checking for updates...
    Welcome to AeroFS Team Server.
    Admin email: matt@aerofs.com
    If you forgot your password, go to
    https://share.syncfs.com/request_password_reset to reset it.
    Admin password: 
    Computer name [ubuntu64]: 
    The following storage options are available:
     0. Store files on the local disk
     1. Store compressed files on the local disk
     2. Store files on Amazon S3 or OpenStack Swift
    Storage option [0]: 0
    Data Storage folder [/home/aerofs/AeroFS Team Server Storage]: 
    Enable mobile and Web access? See https://support.aerofs.com/entries/29044194 for more information.
    [Y]es / [N]o: Y
    API access is enabled.
    Signing in...
    Registering new device...
    You can now access AeroFS Team Server functions through the "aerofsts-sh" command while aerofsts-cli is running.
    Up and running. Enjoy!
    ^C

    Downloading and installing upstart script...
    update-rc.d: warning: /etc/init.d/aerofsts missing LSB information
    update-rc.d: see <http://wiki.debian.org/LSBInitScripts>
     Adding system startup for /etc/init.d/aerofsts ...
       /etc/rc0.d/K20aerofsts -> ../init.d/aerofsts
       /etc/rc1.d/K20aerofsts -> ../init.d/aerofsts
       /etc/rc6.d/K20aerofsts -> ../init.d/aerofsts
       /etc/rc2.d/S20aerofsts -> ../init.d/aerofsts
       /etc/rc3.d/S20aerofsts -> ../init.d/aerofsts
       /etc/rc4.d/S20aerofsts -> ../init.d/aerofsts
       /etc/rc5.d/S20aerofsts -> ../init.d/aerofsts

    Starting AeroFS Service...
    aerofsts start/running, process 2109
    Manage with: sudo service aerofsts <stop|start|restart|status>

    Installation Complete!
    Thanks for using the AeroFS Quick Installation Utility!
