#!/usr/bin/python3
# Author V.Varbanovski @nu11secur1ty
# v-1.0
import ipaddress
for ip in ipaddress.IPv4Network('192.168.1.0/24'):
    host = "facebook.login.com >> %hostspath%"
    print("echo",'',ip,'','','',host)
