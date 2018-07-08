#!/usr/bin/python
# 2018 by Shiva @ CPH:SEC & Cyberium


# Script begins
# ===============================================================================

try:
    from colorama import init
    from termcolor import cprint
    from pyfiglet import figlet_format  # For banner
    import argparse
    import socket
    import threading
    import nmap
    import sys  # for exceptions
    import os  # for os exceptions
except ModuleNotFoundError:
    print('Run pip install -r requirements.txt')
except RuntimeError:
    print('Something went wrong! Module Import Runtime Error')

# Banner =========================================================================
version = '0.0.1'
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
cprint(figlet_format('RoboMap', font='graffiti'), 'green')
print('v. ' + version + ' by Shiva @ CPH:SEC')


def mapper(target, arguments):  # tests if host is up with the nmap -sn  -Pn host
    nmscan = nmap.PortScanner()
    nmscan.scan(hosts=target, arguments='-sn -Pn')
    status = nmscan.scanstats()
    state = 'down'
    # print(str(state) + " " + status['uphosts'])
    if status['uphosts'] == "1":
        state = 'up'
    print('Host: ' + str(target) + " is " + str(state))


def handler():
    print('This is the handler')


def threader():
    print('The Threader')


def smbhandler():
    print('Handler for SMB')


def main():
    try:
        # Arguments
        parser = argparse.ArgumentParser(description='RoboMap ' + 'vs ' + version)
        parser.add_argument("target", help='Target that should be scanned')
        args = parser.parse_args()
        # Variables
        target = args.target
    except RuntimeError as e:
        print('Runtime error: ' + str(e))


if __name__ == "__main__":
    main()
