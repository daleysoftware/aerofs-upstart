import sys
import subprocess
import os
import signal
import urllib2
import traceback

from colorama import Fore, Style

# ------------------------------------------------------------
# Signal Handling
# ------------------------------------------------------------

cli_process = None
exiting = False

def global_signal_handler(s, f):
    global cli_process
    global exiting

    if cli_process is not None:
        cli_process.send_signal(signal.SIGTERM)
        cli_process = None
    else:
        exiting = True
        print
        print
        print Fore.RED + "Received signal. Aborting." + Style.RESET_ALL
        sys.exit(1)

def init_global_signal_handler():
    signal.signal(signal.SIGINT, global_signal_handler)

# ------------------------------------------------------------
# User I/O utilities
# ------------------------------------------------------------

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

# ------------------------------------------------------------
# Network
# ------------------------------------------------------------

def chunk_report(bytes_so_far, chunk_size, total_size):
   percent = float(bytes_so_far) / total_size
   percent = round(percent*100, 2)
   sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
   if bytes_so_far >= total_size: sys.stdout.write('\n')

def chunk_read(response, local_file, chunk_size=8192, report_hook=None):
   total_size = response.info().getheader('Content-Length').strip()
   total_size = int(total_size)
   bytes_so_far = 0
   while True:
      chunk = response.read(chunk_size)
      local_file.write(chunk)
      bytes_so_far += len(chunk)
      if not chunk: break
      if report_hook: report_hook(bytes_so_far, chunk_size, total_size)
   return bytes_so_far

# ------------------------------------------------------------
# Infrastructure Related Utils
# ------------------------------------------------------------

def construct_installer_url(config):
    root_pc = "https://" + config["host"] + "/static/installers"
    root_hc = "https://dsy5cjk52fz4a.cloudfront.net"
    root = root_pc if config["pc"] else root_hc
    version = urllib2.urlopen(root + "/current.ver").read().split('=')[1].strip()
    url =  root + "/aerofs%s-installer-%s.deb" % (("ts" if config["ts"] else ""), version)
    return url

def download_file_from(config, url):
    response = urllib2.urlopen(url)
    basename = os.path.join("/tmp", config["host"] + "-" + os.path.basename(url))
    # Do no re-download if we already have the deb on our system.
    if os.path.isfile(basename): return basename
    with open(basename, "wb") as local_file:
        chunk_read(response, local_file, report_hook=chunk_report)
    return basename

def install_deb(filename):
    subprocess.check_call(("sudo dpkg -i %s" % filename).split(' '))

def run_cli(config):
    global cli_process
    executable = "aerofsts-cli" if config["ts"] else "aerofs-cli"
    cli_process = subprocess.Popen(executable, shell=True)
    return cli_process.wait()

def cert_exists(config):
    cert_filename = "~/.aerofsts/cert" if config["pc"] else "~/.aerofs/cert"
    return os.path.isfile(cert_filename)

# ------------------------------------------------------------
# User Interaction Section
# ------------------------------------------------------------

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
        print Fore.GREEN + "Please enter the DNS hostname of your Appliance." + Style.RESET_ALL
        config["host"] = get_text("PC Appliance DNS Host")
    else:
        config["host"] = "aerofs.com"

    print
    print Fore.GREEN + "Downloading and installing AeroFS..." + Style.RESET_ALL
    installer_url = construct_installer_url(config)
    installer_filename = download_file_from(config, installer_url)
    install_deb(installer_filename)
    #os.unlink(installer_filename)

    print
    print Fore.GREEN + "Running AeroFS installation program..." + Style.RESET_ALL
    print Fore.BLUE + "Press CTRL-C to stop the CLI when setup is finished." + Style.RESET_ALL
    exit_code = run_cli(config)
    if exit_code != -15:
        print
        print Fore.RED + "It looks like the CLI exited abnormally. Aborting." + Style.RESET_ALL
        sys.exit(2)
    if not cert_exists(config):
        print
        print
        print Fore.RED + "It looks like your setup never finished. Aborting." + Style.RESET_ALL
        sys.exit(3)

    print
    print
    print "--- TODO"

    # TODO finish this. Upstart, and aerofs user.

# ------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------

if __name__ == "__main__":
    try:
        init_global_signal_handler()
        main()
    except SystemExit as e:
        raise e
    except:
        print
        print Fore.RED + "Exception caught. Aborting." + Style.RESET_ALL
        traceback.print_exc(file=sys.stdout)
        sys.exit(4)
