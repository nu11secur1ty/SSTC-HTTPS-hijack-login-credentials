#!/usr/bin/bash
# Author @nu11secur1ty
# v-1.0
echo "";
cat /dev/null > /var/log/apache2/access.log
echo -e "\e[33mWelcome to *Hijack HTTPS Listener*\e[0m"
echo -e "\e[32mPress Ctrl + C when you sure have victim already visited your site\e[0m";
	echo "";
tail -f /var/log/apache2/access.log
	exit 0;
