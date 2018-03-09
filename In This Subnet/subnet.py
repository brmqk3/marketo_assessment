import argparse
from netaddr import IPNetwork, IPAddress
import os
import socket
import struct

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, help='The path to the file containing subnets and ips')
parser.add_argument('--output_file', required=True, help='The path to the file outputting true or false')
args = parser.parse_args()

if os.path.isfile(args.output_file):
    os.remove(args.output_file)

input_dict = {}
with open(args.input_file, 'r') as input:
    for line in input.readlines():
        ip, subnet = line.split(',')
        addr_long = socket.ntohl(int(ip, 16))
        ipv4 = socket.inet_ntoa(struct.pack("<L", addr_long))
        in_subnet = False
        with open(args.output_file, 'a+') as output:
            if IPAddress(ipv4) in IPNetwork(subnet):
                in_subnet = True
            output.write("IP: %s, Subnet: %s, In Subnet: %s\n" % (ip, subnet.rstrip(), in_subnet))
