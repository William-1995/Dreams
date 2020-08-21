import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
# client.send("willl".encode("utf8"))
# data = client.recv(1024)
# print (data.decode("utf8"))
# client.close()

while True:
    re_data = input()
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    str = data.decode("utf8")
    if str == 'exit':
        break;
    print(data.decode("utf8"))

client.close()    