#!/usr/bin/python3
# 2018 by Shiva @ CPH:SEC & Cyberium


# Script begins
# ===============================================================================

version = '0.0.1a'

# targetname = '10.10.10.83'
# pingscan = ' -sn -Pn'
# tcpscan = ' -sS -T4 -Pn -open -p- -oX ' + targetname + ' -vv'
# servicescan = ' -sV'



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
    print('Running nmap on ' + target + ' with arguments: ' + arguments)
    nmscan = nmap.PortScanner()  # Constructing object
    nmscan.scan(hosts=target, arguments=arguments)  # test if target is up
    # something


def upcheck(target):
    nm = nmap.PortScanner()  # Constructing object nm
    nm.scan(hosts=target, arguments='-sn -Pn -PE')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for x, status in hosts_list:
        print("[+] " + x + " is " + status)


def reader():
    print('Reads the output')


def handler():
    print('This is the handler')


def threader(function, arguments):
    t = threading.Thread(target=function, args=arguments)
    t.start()


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
        # Calls
        upcheck(target)
        arguments = ' -sS -Pn -p- -open -vv -T4'
        mapper(target, targetname, arguments)
    except RuntimeError as e:
        print('Runtime error: ' + str(e))


if __name__ == "__main__":
    main()
