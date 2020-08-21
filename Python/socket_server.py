import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
# sock, addr = server.accept()

# data = sock.recv(1024)
# print(data.decode("utf8"))
# sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))
# server.close()
# sock.close()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        receive_data = data.decode("utf8")
        print(receive_data)
        if receive_data == 'exit':
            break;
        re_data = input()
        sock.send(re_data.encode("utf8"))    
    server.close()
    sock.close()

while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock,addr))
    client_thread.start()