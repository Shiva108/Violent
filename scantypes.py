#!/usr/bin/python3
# 2018 by Shiva @ CPH:SEC & Cyberium

import nmap

openports = ' 22,80,8080'
target = '10.10.10.83'
targetname = "test_run"
pingscan = ' -sn -Pn'
tcpscan = ' -sS -T4 -Pn -open -p- -vv'
servicescan = ' -sSV -T4 -Pn -vv -p' + openports + ' ' + target


print(pingscan)
print(tcpscan)
print(servicescan)
print('\n')


def mapper(target, targetname, arguments):  # test target with parameters
    nmscan = nmap.PortScanner()  # Constructing object
    nmscan.scan(hosts=target, arguments=arguments)  # test if target is up
    # something
    #   print('[+] Host: ' + str(target) + " is " + str(state))
    print('Running nmap on ' + target + ' with arguments: ' + arguments)


def main():
    try:
        # mapper(target, targetname, pingscan)
        mapper(target, targetname, tcpscan)
        # mapper(target, targetname, servicescan)
    except RuntimeError as e:
        print('Runtime error: ' + str(e))


if __name__ == "__main__":
    main()
