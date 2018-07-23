import os
import socket
import sys


def grabber(target, openports):  # TCP connection attempt + banner grab
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.settimeout(1)
        conn_skt.connect((target, int(openports)))
        conn_skt.send(b'Information\r\n')
        results = str(conn_skt.recv(100))
        results = results[1:99]
        print('[+] tcp ' + str(openports) + " open " + '\nBanner: ' + results + '\n')
        conn_skt.close()
    except socket.timeout or ConnectionRefusedError or ConnectionError:
        print('[-] tcp ' + str(openports) + ' closed')
        return


def main():
    if not os.geteuid() == 0:
        sys.exit("\nYou'r not root - run sudo\n")
    try:
        grabber(target='210.190.155.224', openports='21')  # https://www.shodan.io/host/210.190.155.224
    except RuntimeError as e:
        print('Runtime error: ' + str(e))


if __name__ == "__main__":
    main()
