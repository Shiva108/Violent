#!/usr/bin/python3
# 2018 by Shiva @ CPH:SEC & Cyberium


# Script begins
# ===============================================================================

version = '0.0.2a'

# Control Vars - Change these to change function of script
openports = ' 22,80,8080'
target = '10.10.10.83'
# targetname = "test_run" # For debugging purposes only
pingscan = ' -sn -Pn'
tcpscan = ' -sS -T4 -Pn -open -p- -vv'
servicescan = ' -sSV -T4 -Pn -vv -p' + openports + ' ' + target
outputdir = "~/"
tunning = ' -T4 '  # Todo // for future version

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
    try:
        print('[+] Running nmap on ' + target + ' with arguments: ' + arguments)
        nmscan = nmap.PortScanner()  # Constructing object
        nmscan.scan(hosts=target, arguments=arguments)
    except BaseException as e:
        print('Mapper has crashed: ' + e)
    # print('Mapping ' + target + ' with ' + arguments + ' is done without errors \n')
    for host in nmscan.all_hosts():
        # print('----------------------------------------------------')
        # print('Host : %s (%s)' % (host, nmscan[host].hostname()))
        # print('State : %s' % nmscan[host].state())
        for proto in nmscan[host].all_protocols():
            print('--------------------------------')
            print('[+] Protocol : %s' % proto)
            lport = list(nmscan[host][proto].keys())
            lport.sort()
            for port in lport:
                print('[+] port : %s\tstate : %s' % (port, nmscan[host][proto][port]['state']))



def upcheck(target):
    nm = nmap.PortScanner()  # Constructing object nm
    nm.scan(hosts=target, arguments='-sn -Pn -PE')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for x, status in hosts_list:  # For a possible multi target in later vs.
        print("[+] " + x + " is " + status)


def outputter():
    print('The outputter')

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
    try:
        banner(version)
        # Test for root
        if not os.geteuid() == 0:
            sys.exit("\nYou'r not root - run sudo\n")
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
        # arguments = pingscan
        # mapper(target, targetname, pingscan)
        mapper(target, targetname, ' -sV -p 80,22 -Pn -vv -T4')
    except RuntimeError as e:
        print('Runtime error: ' + str(e))


if __name__ == "__main__":
    main()
