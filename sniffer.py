from scapy.all import sniff
def start(callback):
    sniff(prn=callback,store=False)
