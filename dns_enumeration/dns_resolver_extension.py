from dns import resolver
from dns import reversename

alvo = ("google.com")

resultado = resolver.resolve(alvo, 'A',) # IPV4

for ipv4 in resultado:
    print(f"Registro IPV4: {ipv4}")
    ip_alvo = ipv4.to_text()

print("----")

try:
    resultado = resolver.resolve(alvo, 'CNAME') # real name
    for cname in resultado:
        print(f"Registros CNAME: {cname.target}")
except:
    pass

print("----")

resultado = resolver.resolve(alvo, 'AAAA') # IPV6

for ipv6 in resultado:
    print(f"Registros IPV6: {ipv6}")

print("----")

nome_reverso = reversename.from_address(ip_alvo)
resultado = resolver.resolve(nome_reverso, "PTR")

for ip in resultado:
    print(f"Registros PTR: {ip}")

print("----")

resultado = resolver.resolve(alvo, 'NS',) # IPV4

for ipv4 in resultado:
    print(f"Registro NS: {ipv4}")

print("----")

resultado = resolver.resolve(alvo, 'MX',) # IPV4

for exdata in resultado:
    print(f"Registro MX: {exdata}")

resultado = resolver.resolve(alvo, "SOA",) # IPV4

for ipv4 in resultado:
    print(f"Registro SOA: {ipv4}")

resultado = resolver.resolve(alvo, 'TXT',) # IPV4

for ipv4 in resultado:
    print(f"Registro TXT: {ipv4}")