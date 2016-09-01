#!/usr/bin/env python

import dpkt,sys

if len(sys.argv) < 3:
    print "Usage: ./capglue.py pcap_file out_file"

file_pcap = open(sys.argv[1])
pcap = dpkt.pcap.Reader(file_pcap)
file_rtp = sys.argv[2]

with open(file_rtp,"w") as file_out:
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        tcp = eth.data.data
        if len(tcp.data) > 0:
            rtp = dpkt.rtp.RTP(tcp.data)
            file_out.write(rtp.data)

file_pcap.close()
