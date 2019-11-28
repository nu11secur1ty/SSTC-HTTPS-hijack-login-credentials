#!/usr/bin/python3
# by nu11secur1ty
import snifhttp
import colorama
from colorama import Fore, Style

iface = input("Type the sniffing interface\n")
try:
    snifhttp.sniffing(iface)
 
except KeyboardInterrupt:
    print(Fore.YELLOW + 'Exit...')
