import whois

dominio = input("digite o dominio alvo:")

consulta = whois.whois(dominio)

print(consulta.text)