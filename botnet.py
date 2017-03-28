#!/usr/bin/python
# -*- coding: utf-8 -*-
from pexpect import pxssh
import optparse
import argparse


class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e, '[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetcommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host + '[+] ' + output)


def addclient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)


botNet = []
addclient('127.0.0.1', 'root', 'toor')
addclient('127.0.0.1', 'root', 'toor')
addclient('127.0.0.1', 'root', 'toor')

botnetcommand('uname -v')
botnetcommand('cat /etc/issue')
