import socket

dominio = input("Digite o dominio alvo: ")
brute = ["ns1", "ns2", "ns3", "www", "mail"]

for nome in brute:
    DNS = nome + "." + dominio
    try:
        print(DNS + ":" + socket.gethostbyname(DNS)) # pegando IP atraves do nome de domino
    except socket.gaierror: # exibiria os erros de DNS
        pass

