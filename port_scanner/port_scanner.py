import socket

target = input("Digite o host alvo: ")
ports = [21, 22, 23, 53, 80, 443, 8080]

# for port in range(1000):
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    if result == 0:
        print(port)
