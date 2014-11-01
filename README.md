AeroFS Upstart
===

In this repository you will find an example upstart script for AeroFS.

N.B. these scripts are not officially endorsed by AeroFS at this time.

Quick Install
---

** Quick Install path is still in development **

Run the quick-install script and follow the prompts. This will download the
AeroFS or AeroFS Team Server debian, install it, create an aerofs user and
configure upstart.

This is the best way to install AeroFS on Ubuntu in most cases.

A convenient one-line shell command to execute this script without downloading
this repository:

    bash <(curl -s https://raw.githubusercontent.com/mpillar/aerofs-upstart/master/quick-install.sh)

Or, an even shorter version:

    TODO

Manual Install
---

Copy this script to /etc/init/ and perform the following actions:

    sudo chown root:root /etc/init/aerofs[ts].conf
    sudo service aerofs[ts] start

You will also need to change the user ID in the script (in this example the
user is "aerofs").
