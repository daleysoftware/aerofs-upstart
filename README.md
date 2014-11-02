AeroFS Upstart
===

In this repository you will find an example upstart script for AeroFS.

N.B. these scripts are not officially endorsed by AeroFS at this time.

Quick Install
---

** Quick Install path is still in development **

Run the quick-install script and follow the prompts for a guided install
experience. The AeroFS or AeroFS Team Server debian will be downloaded
autmatically and installed. An an aerofs user will be created and upstart
will be configured for you.

This is the best way to install AeroFS on headless Ubuntu in most cases.

A convenient one-line shell command to execute this script without having to
clone this repository:

    bash <(curl -sL http://ae.ro/1zW1mQG)

Manual Install
---

Copy this script to /etc/init/ and perform the following actions:

    sudo chown root:root /etc/init/aerofs[ts].conf
    sudo service aerofs[ts] start

You will also need to change the user ID in the script (in this example the
user is "aerofs").

Dependencies
---

- Python 2.x
- The following python modules: colorama
