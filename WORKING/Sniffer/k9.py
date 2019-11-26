#!/usr/bin/python3
# by nu11secur1ty
import shifhttp
iface = input("Type the sniffing interface\n")
try:
    shifhttp.sniffing(iface)
 
except KeyboardInterrupt:
    print('Exit...')
