#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
	pkt.show()
pkt = sniff(iface='br-21ed52b6f5f8’, filter=’icmp’, prn=print_pkt)

          
