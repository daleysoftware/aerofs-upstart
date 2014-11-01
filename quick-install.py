#!/bin/python
import sys
import signal

def signal_handler(signal, frame):
    print
    print
    print ">> Received signal. Exiting."
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

def get_selection(allowed):
    allowed_map = {}
    for a in allowed:
        allowed_map[str(a)] = a
    while True:
        sys.stdout.write("Enter a number " + str(allowed) + ": ")
        selection = raw_input()
        if selection in allowed_map:
            sys.stdout.write("Selection " + selection + " okay? [Y/n] ")
            confirm = raw_input()
            if confirm == "Y":
                return allowed_map[selection]

def get_text(prompt):
    while True:
        sys.stdout.write(prompt + ": ")
        text = raw_input()
        sys.stdout.write(prompt + " \"" + text + "\" okay? [Y/n] ")
        confirm = raw_input()
        if confirm == "Y":
            return text

def construct_installer_url(config):
    if config["pc"]:
        root = "https://" + config["pc-dns"]
    else:
        root = "https://dsy5cjk52fz4a.cloudfront.net"

    # TODO version and deb.
    return root

def main():
    config = {}
    print ">> AeroFS Quick Installation Utility"

    print
    print ">> Which AeroFS Service would you like to install?"
    print "[0] AeroFS Team Server"
    print "[1] AeroFS"
    config["ts"] = True if get_selection([0, 1]) is 0 else False

    print
    print ">> Are you using AeroFS Private Cloud or AeroFS Hybrid Cloud?"
    print "[0] Private"
    print "[1] Hybrid"
    config["pc"] = True if get_selection([0, 1]) is 0 else False

    if config["pc"]:
        print
        print ">> Please enter the DNS name for your AeroFS Private Cloud Appliance."
        config["pc-dns"] = get_text("PC Appliance DNS")

    print
    print ">> Downloading the AeroFS installer..."
    url = construct_installer_url(config)
    print url

    # TODO finish this.

    print
    print config

if __name__ == "__main__":
    main()
