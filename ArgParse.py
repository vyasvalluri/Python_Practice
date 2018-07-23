#!/usr/bin/env python3

import optparse

#Usage: ArgParse.py [options]

#Options:
 # -h, --help            show this help message and exit
 # -i INTERFACE, --interface=INTERFACE
 #                       interface to change its MAC address
 # -m NEW_MAC, --mac=NEW_MAC
 #                      New MAC address

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

inf = options.interface
mac = options.new_mac

print("entered arguments are %s , %s " % (inf,mac))



