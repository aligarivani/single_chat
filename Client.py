from socket import *
import os
from colorama import Fore, init
os .system('cls')
init()
connect = socket(AF_INET, SOCK_STREAM)

connect.connect(('Server ip', 1234))  # edit here

username = connect.recv(1024).decode()
connect.send(input(Fore.YELLOW+username+Fore.LIGHTBLUE_EX).encode())
passwd = connect.recv(1024).decode()
connect.send(input(Fore.YELLOW+passwd+Fore.LIGHTBLUE_EX).encode())
resualt1 = connect.recv(1024).decode()
os.system('cls')
print(Fore.WHITE+resualt1)
if resualt1 == 'Welcome to chat ':
    while True:
        connect.send(input("MSG >. ").encode())
        msg = connect.recv(1024).decode()
        print(msg)
        if msg == 'exit':
            connect.send('exit'.encode())
            connect.close()
            exit()

connect.close()
