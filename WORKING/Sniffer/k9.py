#!/usr/bin/python3
import k9
iface = input("Type the sniff interface\n")
try:
    k9.sniffing(iface)
 
except KeyboardInterrupt:
    print('Exit...')
