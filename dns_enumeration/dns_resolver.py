from dns_basic import resolver as dns

dominio = input("Digite o dominio alvo: ")
a = ["MX", "NS"]

for registro in a:
    resultado = dns.resolver.query(dominio, registro, raise_on_no_answer=False) # resolver.query() usado para determinar se determinado dominio existe ou nao
    if resultado.rrset is not None:
        print(resultado.rrset) # o .rrset é usado para ele nao trazer o hexadecimal(endereço da memoria), e sim o valor que está neste endereço
