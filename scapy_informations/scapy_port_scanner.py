from reprlib import recursive_repr
from scapy.all import *
from scapy.layers.inet import TCP

target = input("ALVO: ")
ports = [21, 22, 23, 53, 80, 443, 8080]
ip_packet = IP(dst = target)
tcp_packet = TCP(dport=ports, flags="S")
packet = ip_packet/tcp_packet

ans, unans = sr(packet, inter=0.1, timeout=0.1)
print("Porta | Estado")
for receive_packet in ans:
    ports = receive_packet[1][TCP].sport
    flags = receive_packet[1][TCP].flags
    print(f"{ports} | {flags}")
