AeroFS Upstart
==============

This this repository you will find an example upstart script for AeroFS. This upstart script has
been tested on Ubuntu 13.10 server.

To use this script, copy it to /etc/init/ and perform the following action:

    sudo chown root:root /etc/init/aerofs.conf
    sudo service aerofs start

You will also need to change user ID in the script (in this example the user is "mpillar").

Enjoy!
