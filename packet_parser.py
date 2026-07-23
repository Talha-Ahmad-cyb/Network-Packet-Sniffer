from scapy.all import Ether,IP,IPv6,TCP,UDP,ICMP,ARP
def parse(packet):
    return {"summary":packet.summary()}
