#!/usr/bin/python3
import k9
 
try:
    k9.sniffing('ens38')
 
except KeyboardInterrupt:
    print('Exit...')
