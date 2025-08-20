import socket
users = ["root", "sac", "financeiro"]
target = input("ALVO:")

for user in users:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket para conexao SMTP
    sock.connect((target, 25)) #conexao na porta padrao do SMTP
    sock.recv(1024) #recebendo banner do servidor
    sock.send("VRFY" + user + "\n") #envia o objeto VRFY atraves do send para verificar se o user existe
    smtp_resultado = sock.recv(1024)
    sock.close()

    if "252" in smtp_resultado:
        print(f"{user} --> VALIDO!")
    elif "550" in smtp_resultado:
        print(f"{user} --> Invalido!")
    elif "503" in smtp_resultado:
        print(f"{user} --> Requer autenticacao!")
        break
    elif "500" in smtp_resultado:
        print(f"{user} --> VRFY nao suportado pelo servidor!")
        break
    else:
        print(f"resposta do servidor: {smtp_resultado}")