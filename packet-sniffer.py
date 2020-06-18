import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface = interface, store = False, Prn = process_packet)

def process_packet(packet):
    print(packet)

sniff("bridge0")