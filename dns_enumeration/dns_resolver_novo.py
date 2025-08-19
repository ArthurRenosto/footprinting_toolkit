from dns import resolver as dns

alvo = "google.com"

resultado = dns.resolve(alvo, 'a')

for ip in resultado:
    print("IP: ", )