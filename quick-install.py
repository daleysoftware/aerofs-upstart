import sys
import subprocess
import os
import signal
import urllib2
import traceback

from colorama import Fore, Style

cli_process = None
def global_signal_handler(s, f):
    global cli_process
    if cli_process is not None:
        cli_process.send_signal(signal.SIGTERM)
        cli_process = None
    else:
        print
        print
        print Fore.RED + "Received signal. Exiting." + Style.RESET_ALL
        sys.exit(1)

def init_global_signal_handler():
    signal.signal(signal.SIGINT, global_signal_handler)

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

    url =  root + "/aerofs%s-installer-%s.deb" % (("ts" if config["ts"] else ""), version)
    print "URL: %s" % url
    return url

def download_file_from(url):
    f = urllib2.urlopen(url)
    basename = os.path.join("/tmp", os.path.basename(url))
    # Do no re-download if we already have the deb on our system.
    if os.path.isfile(basename):
        return basename
    with open(basename, "wb") as local_file:
        local_file.write(f.read())
    return basename

def install_deb(filename):
    subprocess.check_call(("sudo dpkg -i %s" % filename).split(' '))

def launch_cli(config):
    global cli_process
    executable = "aerofsts-cli" if config["ts"] else "aerofs-cli"
    cli_process = subprocess.Popen(executable, shell=True)
    signal.pause()

def main():
    config = {}
    print Fore.GREEN + "AeroFS Quick Installation Utility" + Style.RESET_ALL
    print "The easist, fastest way to install AeroFS on headless Ubuntu systems."

    print
    print Fore.GREEN + "Which AeroFS Service would you like to install?" + Style.RESET_ALL
    print "[0] AeroFS Team Server"
    print "[1] AeroFS"
    config["ts"] = True if get_selection([0, 1]) is 0 else False

    print
    print Fore.GREEN + "Are you using AeroFS Private Cloud or Hybrid Cloud?" + Style.RESET_ALL
    print "[0] Private"
    print "[1] Hybrid"
    config["pc"] = True if get_selection([0, 1]) is 0 else False

    if config["pc"]:
        print
        print Fore.GREEN + "Please enter the DNS name of your Appliance." + Style.RESET_ALL
        config["pc-dns"] = get_text("PC Appliance DNS")

    print
    print Fore.GREEN + "Downloading and installing AeroFS..." + Style.RESET_ALL
    # TODO need progress meter here.
    installer_filename = download_file_from(construct_installer_url(config))
    install_deb(installer_filename)
    #os.unlink(installer_filename)

    print
    print Fore.GREEN + "Running AeroFS installation program..." + Style.RESET_ALL
    print Fore.BLUE + "Press CTRL-C to stop the CLI when setup is finished." + Style.RESET_ALL
    launch_cli(config)

    # TODO need to fix the signal handling and threading here.

    # TODO finish this.

if __name__ == "__main__":
    try:
        init_global_signal_handler()
        main()
    except:
        print
        print Fore.RED + "Exception caught. Exiting." + Style.RESET_ALL
        traceback.print_exc(file=sys.stdout)
        sys.exit(2)
