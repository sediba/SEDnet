#!/usr/bin/env python

import subprocess
import random
import os
import sys
from string import digits
from string import punctuation
from string import ascii_letters
from requests import get, exceptions


def menu():
	os.system("clear")
	print(""" 
 ____  _____ ____             _                      _    _             
/ ___|| ____|  _ \ _ __   ___| |___      _____  _ __| | _(_)_ __   __ _ 
\___ \|  _| | | | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / | '_ \ / _` |
 ___) | |___| |_| | | | |  __/ |_ \ V  V / (_) | |  |   <| | | | | (_| |
|____/|_____|____/|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\_|_| |_|\__, |
                                                                  |___/ 

		 """)
	print("")
	print("Access the tools by typing <sednet> on the terminal")
	print("")
	print("1 -- Get information about YOUR IP address")	
	print("2 -- Check if you have internet access")
	print("3 -- Change your MAC address")
	print("4 -- WhoIs lookup")
	print("5 -- GeoIP lookup")
	print("6 -- Port scan")
	print("7 -- Reverse IP scan")
	print("8 -- DNS lookup")
	print("9 -- Reverse DNS lookup")
	print("10 -- Traceroute/tracing the path of an Interenet Connection")
	print("11 -- Get all page links from a site")
	print("12 -- Create a new random password")
	print("i -- Update SEDnet")
	print("menu -- whenever you want to see this page again")
	menu_answer = input("SEDnetworking > ")
	
	if menu_answer == "menu":
		menu()

	if menu_answer == "i":
		up()

	elif menu_answer == "1":
		your_ip()

	elif menu_answer == "2":
		internetConnection()
	
	elif menu_answer == "3":
		mac_changer()

	elif menu_answer == "4":
		whois()

	elif menu_answer == "5":
		geoip()

	elif menu_answer == "6":
		portscan()

	elif menu_answer == "7":
		reverseiplookup()

	elif menu_answer == "8":
		dns()

	elif menu_answer == "9":
		reversedns()

	elif menu_answer == "10":
		mtr()

	elif menu_answer == "11":
		pagelinks()

	elif menu_answer == "12":
		srp()

#using mtr an advanced traceroute tool to trace the path of an Internet connection provided by: hackertarget.com
def mtr():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("Tracerouting " + domain)
	os.system("curl https://api.hackertarget.com/mtr/?q=" + domain)
	cont()

#find DNS records for a domain, results are determined using the dig DNS tool provided by: hackertarger.com
def dns():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("... " + domain)
	os.system("curl https://api.hackertarget.com/dnslookup/?q=" + domain)
	cont()

#find Reverse DNS records for an IP address or a range of IP addresses provided by: hackertarget.com
def reversedns():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("... " + domain)
	os.system("curl https://api.hackertarget.com/reversedns/?q=" + domain)
	cont()

#find the location of an IP address using the GeoIP lookup location tool provided by: hackertarget.com
def geoip():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("Getting Geoip info for " + domain)
	os.system("curl https://api.hackertarget.com/geoip/?q=" + domain)
	cont()

#determine the registered owner of a domain or IP address block with the whois tool provided by: hackertarget.com
def whois():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("Getting info based on whois for " + domain)
	os.system("curl https://api.hackertarget.com/whois/?q=" + domain)
	cont()

#determine the status of an Internet facing service or firewall provided by: hackertarget.com
def portscan():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("Portscanning  " + domain)
	os.system("curl https://api.hackertarget.com/nmap/?q=" + domain)
	cont()

#wiscover web hosts sharing an IP address with a reverse IP lookup provided by: hackertarget.com
def reverseiplookup():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("... " + domain)
	os.system("curl https://api.hackertarget.com/reverseiplookup/?q=" + domain)
	cont()

#dump all the links from a web page provided by: hackertarget.com
def pagelinks():
	domain = input("Enter domain name or IP address > ")
	os.system("clear")
	print("Getting page links for " + domain)
	os.system("curl https://api.hackertarget.com/pagelinks/?q=" + domain)
	cont()


#continue after providing the info you requested
def cont():

	tr = input("Continue? y/n > ").lower()
	if tr == "y":
		os.system("clear")
		menu()
	elif tr == "n":
		os.system("clear")
		exit()
	elif tr == "menu":
		os.system("clear")
		menu()
	else:
		os.system("clear")
		cont()

#check if the user is giving the right information to continue (y or n)
def acceptable_value():
	
	print("Enter an acceptable value! (y or n)")

	again = input("Try again? y/n > ")
	
	if again == "y":
		os.system("clear")
		srp()
	elif again == "n":
		os.system("clear")
		exit()
	elif again == "menu":
		os.system("clear")
		menu()
	else:
		os.system("clear")
		acceptable_value()

#a function with user input so they can chose the options for their password	
def srp():

	number_of_characters = int(input("How long should the password be in lengh? > "))

	pc = input("Should the password contain punctuations symbols? y/n > ").lower()

	if pc == "y":

		symbols = ascii_letters + digits + punctuation
		random_process = random.SystemRandom()
		password = "".join(random_process.choice(symbols)
				for i in range(number_of_characters))
		print(password)
		cont()

	elif pc == "n":
 
		symbols = ascii_letters + digits
		random_process = random.SystemRandom()
		password = "".join(random_process.choice(symbols)
				for i in range(number_of_characters))
		print(password)
		cont()

	elif pc == "menu":
		menu()

	else:
		acceptable_value()

#a function in order to change your mac address, based on "ma academy" on youtube
def mac_changer():

	interface = input("Enter your interface (type ifconfig here to see it if you don't know) > ")

	new_mac = input("Enter a custom MAC address (type d to change your MAC address to: 02:a0:04:d3:00:11) > ")

	if new_mac == "d":
	
		print("Changing the MAC address of " + interface + " to 02:a0:04:d3:00:11")
		subprocess.call("ifconfig " + interface + " down", shell=True)
		subprocess.call("ifconfig " + interface + " hw ether 02:a0:04:d3:00:11", shell=True)
		subprocess.call("ifconfig " + interface + " up", shell=True)
	
		print("Your MAC address is changed, check it by typing ifconfig")
		cont()

	else:
	
		print("Changing the MAC address of " + interface + "to " + new_mac)
		subprocess.call("ifconfig " + interface + " down", shell=True)
		subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
		subprocess.call("ifconfig " + interface + " up", shell=True)
		
		print("Your MAC address is changed, check it by typing ifconfig")
		cont()

#a function in order to check if you have internet access or not
def internetConnection():
	try:
		get('https://www.youtube.com/channel/UCfiZlKuoCswXb17JRyEbeJg?view_as=subscriber', timeout = 3)
		print('connected')
		cont()
	except exceptions.ConnectionError:
		print('not connected')
		cont()

#get general information about your ip address based on info provided by: ipinfo.io
def your_ip():
	print("-Your IP address: ")
	os.system("curl https://ipinfo.io/ip") 
	print("-Hostname: ")
	os.system("curl https://ipinfo.io/hostname")
	print("-City: ")
	os.system("curl https://ipinfo.io/city")
	print("-Region: ")
	os.system("curl https://ipinfo.io/region")
	print("-Country: ")
	os.system("curl https://ipinfo.io/country")
	print("-Geolocation: ")
	os.system("curl https://ipinfo.io/loc")
	cont()

#update your script, based on: github.com/Manisso
def up():
	os.system("clear")
	os.system("git clone https://github.com/sediba/SEDnet.git")
	os.system("cd SEDnet && sudo bash ./update.sh")
	os.system("sednet")


menu()
