#!/usr/bin/python3
# by nu11secur1ty
import snifhttp
iface = input("Type the sniffing interface\n")
try:
    snifhttp.sniffing(iface)
 
except KeyboardInterrupt:
    print('Exit...')
