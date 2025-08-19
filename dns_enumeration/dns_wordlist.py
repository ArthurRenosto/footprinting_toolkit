import socket

dominio = input("Digite o dominio alvo: ")

with open("wordlist.txt", "r") as arquivo:
    wordlist = arquivo.readlines()

for nome in wordlist:
    DNS = nome.strip("\n") + "." + dominio
    try:
        print(DNS + ":" + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass
