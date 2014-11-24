AeroFS Upstart
===

In this repository you will find an example upstart script for AeroFS, and some
tools that allow you to easily install and configure AeroFS on headless systems.

N.B. these scripts are not officially endorsed by AeroFS at this time.

Quick Install
---

Run the quick-install script and follow the prompts for a guided install
experience. The AeroFS or AeroFS Team Server debian will be downloaded
autmatically and installed. An an aerofs user will be created and upstart
will be configured for you.

This is the best way to install AeroFS on headless systems in most cases.

A convenient one-line shell command to execute this script without having to
clone this repository:

    bash <(curl -sL https://bit.ly/10dm1z5)

Note that this command must be run as root. [Example](./quick-install-example.md).

Manual Install
---

Copy this script to /etc/init/ and perform the following actions:

    sudo chown root:root /etc/init/aerofs[ts].conf
    sudo service aerofs[ts] start

You will also need to change the user ID in the script (in this example the
user is "aerofs").

Dependencies
---

Quick install requires the following:

- Python 2.x
- The following python modules: colorama
