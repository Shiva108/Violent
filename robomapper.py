#!/usr/bin/python
# 2018 by Shiva @ CPH:SEC & Cyberium


# Script begins
# ===============================================================================

version = '0.0.1a'

try:
    from colorama import init
    from termcolor import cprint
    from pyfiglet import figlet_format  # For banner
    import argparse
    import socket
    import threading
    import nmap  # python-nmap
    import sys  # for exceptions
    import os  # for os exceptions
except ModuleNotFoundError:
    print('Run pip install -r requirements.txt')
except RuntimeError:
    print('Something went wrong! Module Import Runtime Error')


def banner(version):
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    cprint(figlet_format('RoboMap', font='graffiti'), 'green')
    print('v. ' + version + ' by Shiva @ CPH:SEC ' + '\n')


def mapper(target, targetname, arguments):  # test target with parameters
    nmscan = nmap.PortScanner()  # Constructing object
    nmscan.scan(hosts=target, arguments=' -sn -Pn')  # test if target is up
    status = nmscan.scanstats()
    state = 'down'
    # print(str(state) + " " + status['uphosts'])
    if status['uphosts'] == "1":
        state = 'up'
    print('[+] Host: ' + str(target) + " is " + str(state))
    print('Running nmap on ' + target + ' with arguments: ' + arguments)


def upcheck(target):
    # new code
    nm = nmap.PortScanner()  # Constructing object nm
    nm.scan(hosts=target, arguments='-sn -Pn -PE')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.host)


def handler():
    print('This is the handler')


def threader():
    print('The Threader')


def smbhandler():
    print('Handler for SMB')


def bannergrap():
    print('This is a bannergrapper')


def main():
    banner(version)
    try:
        # Arguments
        parser = argparse.ArgumentParser(description='RoboMap ' + 'vs ' + version)
        parser.add_argument("target", help='Target that should be scanned')
        parser.add_argument("-targetname", help='Optional, name of target, for reporting')
        parser.add_argument("-scantype", help='Optional, type of scan to be performed')
        args = parser.parse_args()
        # Variables
        target = args.target
        targetname = args.targetname
        scantype = args.scantype
        #
        upcheck(target)
        # mapper(target, targetname, ' -sS -Pn -vv --top-ports 100')
    except RuntimeError as e:
        print('Runtime error: ' + str(e))


if __name__ == "__main__":
    main()
