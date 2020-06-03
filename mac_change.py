#!/usr/bin/env python3

import subprocess
import re


def welcome():
    print(25 * "*" + "\nMAC Changer\nby Ovi\n" + 25 * "*")
    p0 = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
    p0 = p0.stdout
    c0 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",p0)  
    c01 = str(c0.group(0))   
    return print("Your current mac address is: " + c01)

def changeMac():
    interface = input("Enter your instance: ")
    mac_address = input("Enter your new mac address: ")

    subprocess.call(['sudo', 'ifconfig', interface,'down' ])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac_address ])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    return mac_address
    
def checkResults():
    p1 = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
    p1 = p1.stdout
    c = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",p1)
    return c.group(0)

def success(regex,mac):
    if regex == mac:
        print("Mac Address was succesfully change to " + mac)
    else:
        print("Mac Address failed to be changed")

welcome()
result = changeMac()
r = checkResults()
success(result,r)


