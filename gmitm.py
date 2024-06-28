from scapy.config import conf
from scapy.all import PcapWriter, AsyncSniffer
import os
import datetime

RESPOND = 1
FORWARD = 2
IGNORE = 3

class iface():
    def __init__(self, name):
        self.name = name
        self.sock = conf.L2socket(name)
        self.sniff = None

class gmitm():
    def __init__(self, elab, iface1, iface2):
        self.elab = elab
        self.iface1 = iface(iface1)
        self.iface2 = iface(iface2)
        self.pcapfile = PcapWriter("./loot/" + datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S") + "-loot.pcap")

    def stop(self):
        os.system("iptables -D INPUT -j ACCEPT")
        os.system("iptables -D OUTPUT -j ACCEPT")
        os.system("iptables -D FORWARD -j ACCEPT")
        self.iface1.sniff.stop()
        self.iface2.sniff.stop()

    def start(self):
        os.system("iptables -A INPUT -j DROP")
        os.system("iptables -A OUTPUT -j DROP")
        os.system("iptables -A FORWARD -j DROP")

        def initelab1(packet):
            self.elaboration(self.iface1, self.iface2, packet)
        self.iface1.sniff = AsyncSniffer(iface=self.iface1.name, prn=initelab1, filter="inbound")

        def initelab2(packet):
            self.elaboration(self.iface2, self.iface1, packet)
        self.iface2.sniff = AsyncSniffer(iface=self.iface2.name, prn=initelab2, filter="inbound")

        self.iface1.sniff.start()
        self.iface2.sniff.start()

    def elaboration(self, srciface, dstiface, originpacket):
        operation, elabpacket, save = self.elab(srcinterface.name, originpacket)
        try:
            if operation == RESPOND:
                srciface.sock.send(elabpacket)
            elif operation == IGNORE:
                pass
            elif operation == FORWARD:
                dstiface.sock.send(elabpacket)
        except:
            pass
        if save == True:
            self.pcapfile.write(elabpacket)
