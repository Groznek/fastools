import os
import getpass 
import platform 
import subprocess 
import sys
import time
import socket
import random
import shutil  
import subprocess as sp  
import random
import string
from datetime import date
import datetime
from time import sleep
import requests
from colorama import Fore
#UTF8 dev by /*!APAI*/
system = True
dl = input("Download all tools yes/no ? ")
dlyes = "yes"
dlno = "no"
if dl == dlyes:
    os.system("cd Bureau")
    #os.system("apt install python3")
    #os.system("apt install python3-pip")
    os.system("git clone https://github.com/v0re/dirb.git")
    os.system("git clone https://github.com/laramies/theHarvester.git")
    os.system("git clone https://github.com/Groznek/CSRF-0-Protection.git")
    os.system("git clone https://github.com/Groznek/rcetools.git")
    os.system("git clone https://github.com/Groznek/bruteforcetools.git")
    os.system("git clone https://github.com/s0md3v/XSStrike.git")
    #os.system("apt-get update")
    os.system("clear")
elif dl == dlno:
    print("\u001b[31mEnjoy :)\u001b[0m")
    time.sleep(2)
    os.system("clear")

else:
    print("Error")
    time.sleep(20)
    os.system("clear")
#choix fast/skid
choix= input("Optimize pentest [1] or User System [2] >  ")
opt = "1"
longg = "2"
#pentest choix
if choix == opt:
        os.system("clear")
        while system:

            print("\t \u001b[36m[MENU]\u001b[0m")
            print("\t Dev by Apai | Twitter : @vesahru")
            print("\u001b[36;1m[+]\u001b[0m nmap scan sV : [1]")
            print("\u001b[36;1m[+]\u001b[0m dirb scan : [2]")
            print("\u001b[36;1m[+]\u001b[0m curl source : [3]")
            print("\u001b[36;1m[+]\u001b[0m Osint scan domain : [4]")
            print("\u001b[36;1m[+]\u001b[0m CSRF 0 protect script : [5]")
            print("\u001b[36;1m[+]\u001b[0m vsftp paylaod : [6]")
            print("\u001b[36;1m[+]\u001b[0m RCE tools : [7]")
            print("\u001b[36;1m[+]\u001b[0m nmap packet trace : [8]")
            print("\u001b[36;1m[+]\u001b[0m Clear all: [9]")
            choice = input("\u001b[31mEnter your choice : \u001b[0m")
#Choix 1

            if choice == "1":
                
                url1 = input("Enter url : ")
                print("\u001b[36;1m[+]\u001b[0m Scan launch...")
                os.system("nmap -sV "+ url1)
                clearr = input("Clear ? yes/no : ")
                yes1 = "yes"
                no1 = "no"
                if clearr == yes1:
                    print("\u001b[36;1m[+]\u001b[0m Clear..")
                    time.sleep(2)
                    os.system("clear")
                    print("\u001b[31;1m[+] Scan clear !\u001b[0m")
                    time.sleep(1)
                    os.system("clear")
                    print("Scan clear !")
                elif clearr == no1:
                    print("\u001b[31;1m[+] No Clear !\u001b[0m ")
                else:
                    print("Error")
# Choix 2
            elif choice == "2":
                url2 = input("Enter url : ")
                os.system("dirb "+ url2)
                clearrr = input("Clear ? yes/no : ")
                yes2 = "yes"
                no2 = "no"
                if clearrr == yes2:
                    print("\u001b[36;1m[+]\u001b[0m Clear..")
                    time.sleep(2)
                    os.system("clear")
                    print("\u001b[31;1m[+] Scan Clear !\u001b[0m")
                    time.sleep(1)
                    os.system("clear")
                elif clearrr == no2:    
                    print("\u001b[31;1m[+] No Clear !\u001b[0m")
                else:
                    print("Error")
#choix 3
            elif choice == "3":
                
                url3 = input("Enter url : ")
                os.system("curl -s "+ url3)
                sup = input("Clear ? yes/no : ")
                yes3 = "yes"
                no3 = "no"
                if sup == yes3: 
                    print("\u001b[36;1m[+]\u001b[0m Clear..")
                    time.sleep(2)  
                    os.system("clear")
                    print("\u001b[31;1m[+] Scan Clear !\u001b[0m")
                    time.sleep(1)
                    os.system("clear")
                elif sup == no3:
                    print("\u001b[31;1m[+] No Clear !\u001b[0m")
                else:
                    print("Error")
#Choix 4
            elif choice == "4":
                
                print("Exemple : domain.com")
                url4 = input("Source : google [1] | linkedin [2] | yahoo [3] : ")
                google = "1"
                linkedin = "2"
                yahoo = "3"
                time.sleep(1)
                if url4 == google:
                    urlharvester = input("Enter Domain : ")
                    os.system("theHarvester -l 500 -b google -d"+ urlharvester)
                    clear = input("Clear ? yes/no : ")
                    yes4 = "yes"
                    no4 = "no"
                    if clear == yes4:
                        print("\u001b[36;1m[+]\u001b[0m Clear..")
                        time.sleep(2)
                        os.system("clear")
                        print("\u001b[31;1m[+] Scan Clear !\u001b[0m")
                        time.sleep(1)
                        os.system("clear")
                    elif clear == no4:
                        print("\u001b[31;1m [+]No Clear !\u001b[0m")
                elif url4 == linkedin:       
                    urlharvester = input("Enter Domain : ")
                    os.system("theHarvester -l 500 -b linkedin -d"+ urlharvester)
                    caca = input("Clear ? yes/no : ")
                    yes41 = "yes"
                    no41 = "no"
                    if caca == yes41:
                        print("\u001b[36;1m[+]\u001b[0m Clear..")
                        time.sleep(2)     
                        os.system("clear")
                        print("\u001b[31;1m[+] Scan Clear !\u001b[0m")
                        time.sleep(1)
                        os.system("clear")
                    elif caca == no41: 
                        print("\u001b[31;1m [+]No Clear !\u001b[0m")
                    else:
                        print("Error")
                elif url4 == yahoo:
                    urlharvester = input("Enter Domain : ")
                    os.system("theHarvester -l 500 -b yahoo -d"+ urlharvester)
                    zizi = input("Clear ? yes/no : ")
                    yes42 = "yes"
                    no42 = "no"
                    if zizi == yes42:
                        print("\u001b[36;1m[+]\u001b[0m Clear..")
                        time.sleep(2)
                        os.system("clear")
                        print("\u001b[31;1m[+] Scan Clear !\u001b[0m")
                        time.sleep(1)
                        os.system("clear")
                    elif zizi == no42:
                        print("\u001b[31;1m [+]No Clear !\u001b[0m")
                    else:
                        print("Error")
                else:
                    print("Error")
#Choix 5
            elif choice == "5":
                print("\u001b[36;1m[+]\u001b[0m Chargement .")
                time.sleep(1)
                os.system("clear")
                print("\u001b[36;1m[+]\u001b[0m Chargement ..")
                time.sleep(1)
                os.system("clear")
                print("\u001b[36;1m[+]\u001b[0m Chargement ...")
                time.sleep(1)
                os.system("clear")
                print("HTML CSRF")
                os.system("open register.html")
                os.system("nano register.html")
#Choix 6  
            elif choice == "6":
                print("\u001b[36;1m[+]\u001b[0m search vsftpd payload !")
                time.sleep(2)
                print("In metasploit search : vsftpd with search vsftpd")
                time.sleep(3)
                os.system("msfconsole")
#Choix 7
            elif choice == "7":
                print("\u001b[36;1m[+]\u001b[0m RCE tools ..")
                time.sleep(1)
                os.system("cd cve-2020-0688/")
#Choix 8
            elif choice == "8":
                print("\u001b[36;1m[+]\u001b[0m Packet trace..")
                time.sleep(2)
                print("Exemple : www.host.com")
                packet = input("Enter Host :")
                os.system("nmap --packet-trace "+ packet)
                packetclear = input("Clear Scan ? yes/no : ")
                yes8 = "yes"
                no8 = "no"
                if packetclear == yes8:
                    print("\u001b[36;1m[+]\u001b[0m Clear..")
                    time.sleep(2)
                    os.system("clear")
                    print("\u001b[31;1m[+] Scan Clear !\u001b[0m")
                    time.sleep(1)
                    os.system("clear")
                elif packetclear == no8:
                    print("\u001b[31;1m [+]No Clear !\u001b[0m")
                else:
                    print("Error")
#Choix 9 / clear
            elif choice == "9":
                os.system("clear")
                print("\u001b[31;1m[+] Clear !\u001b[0m")
                time.sleep(2)
                os.system("clear")
            else:
                print("Error")
                time.sleep(1)
                os.system("clear")
                
elif choix == longg:
    os.system("clear")
    root = input("Enter your root name > ")
    while system:
        print("\t \u001b[36;1m [MENU]\u001b[0m")
        print("\u001b[36;1m[+]\u001b[0m Doxbase [1]")
        print("\u001b[36;1m[+]\u001b[0m BruteForceInstagram [2]")
        user = input("root@"+root+ " :")
        if user == "1":
            print("\t \u001b[36;1m[+]\u001b[0m Chargement Doxbase..")
            doxbase = input("Site [1] | Discord [2] : ")
            doxbasesite = "1"
            doxbasediscord = "2"
            if doxbase == doxbasesite:
                print("\u001b[36;1mLink : https://doxbase.cc\u001b[0m")
                time.sleep(8)
                os.system("clear")
                
            elif doxbase == doxbasediscord:
                print("\u001b[36;1mLink : discord.gg/doxbase\u001b[0m")
                time.sleep(8)
                os.system("clear")
            else:
                print("Error")
        elif user == "2":
            print("\t \u001b[36;1m[+]\u001b[0m Chargement BruteForce..")
            os.system("python3 bruteforce.py")
            time.sleep(15)
            os.system("clear") 
        elif user == "3":
            print("\t \u001b[36;1m[+]\u001b[0m Chargement XSStrike..")
            os.system("cd XSStrike/")
            os.system("python3 xssstrike.py")
            print("\u001b[31m To [+] launch the .py, remove it from its folder\u001b[0m")
        elif user == "clear":
            os.system("clear")



else:
    print("Error")



