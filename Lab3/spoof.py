#!/usr/bin/env python3
from scapy.all import *
ip = IP()
ip.dst = '10.9.0.1'
ip.src = '1.2.3.4'
icmp = ICMP()

packet = ip/icmp
