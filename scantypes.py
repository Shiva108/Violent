#!/usr/bin/python3
# 2018 by Shiva @ CPH:SEC & Cyberium

import nmap

targetname = '10.10.10.83'
pingscan = ' -sn -Pn'
tcpscan = ' -sS -T4 -Pn -open -p- -oA ' + targetname + ' -vv'
servicescan = ' -sV'

print(targetname)
print(pingscan)
print(tcpscan)
print(servicescan)


def mapper(target, targetname, arguments):  # test target with parameters
    nmscan = nmap.PortScanner()  # Constructing object
    nmscan.scan(hosts=target, arguments=arguments)  # test if target is up
    # something
    #   print('[+] Host: ' + str(target) + " is " + str(state))
    print('Running nmap on ' + target + ' with arguments: ' + arguments)
