from socket import *


server = socket(AF_INET, SOCK_STREAM)

server.bind(('your ip', 1234))

server.listen(1)

client, address = server.accept()

client.send('User Name : '.encode())
user_name = client.recv(1024).decode()
print(f'user name > {user_name}')
if user_name == 'test1':
    client.send("password : ".encode())
    passwd = client.recv(1024).decode()
    print(f'passwd > {passwd}')
    if passwd == 'test1':
        client.send('Welcome to chat '.encode())
        while True:
            msg = client.recv(1024).decode()
            print(msg)
            client.send(input('MSG >. ').encode())
            if msg == 'exit':
                client.send('exit'.encode())
                client.close()
                exit()
    else:
        client.send('passwd is False '.encode())
else:
    client.send('User Name Not Found !'.encode())

server.close()
