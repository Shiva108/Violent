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
    print('Make sure modules are installed correctly! ')
except RuntimeError:
    print('Something went wrong! Module Import Runtime Error')

# Banner

version = '0.0.1'
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

cprint(figlet_format('RoboMap', font='graffiti'), 'blue')
print('v. ' + version)
