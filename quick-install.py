import sys
import os
import signal
import urllib2

def signal_handler(s, f):
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
        root = "https://" + config["pc-dns"] + "/static/installers"
    else:
        root = "https://dsy5cjk52fz4a.cloudfront.net"
    version = urllib2.urlopen(root + "/current.ver").read().split('=')[1].strip()
    return root + "/aerofs%s-installer-%s.deb" % (("ts" if config["ts"] else ""), version)

def download_file_from(url):
    f = urllib2.urlopen(url)
    basename = os.path.basename(url)
    print "URL: %s" % url
    with open(os.path.basename(url), "wb") as local_file:
        local_file.write(f.read())
    return basename

def install_deb(filename):
    # TODO
    pass

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
    install_deb(download_file_from(construct_installer_url(config)))

    # TODO finish this.

    print
    print config

if __name__ == "__main__":
    main()
