# Username enumeration via response timing

This lab was bit tricky for me and figuring it out took quite a bit of my time. To simplify the objectives of this lab:- 

- **First**, there is ip-based rate limiting to prevent brute force attempts. So, I used the `X-Forwarded-For` header to bypass this. I created a list of 255 hosts and rotated through them with each request.
- **Second**, to get a valid username I'd set the password to a 1000 characters long string. Setting the password to a very long string will make the webapp take longer than usual to process the password thus resulting in a `timing` difference. Decreasing this value will decrease the response times.
- **Third**, I've taken a four seconds delay as base for my timing attack. Note, timing based things are a bit finicky and these values can be completely different for you based on your internet connection and the location where you live. The response times are generally more than 4 seconds for me, but YMMV.🙂 



I've added two bash scripts, one for bruteforcing the username and the other for password. I've also added a file containing 255 ips. If you want to generate your own you can use this command:
```
for ((i=1;i<256;i+=1)); do echo "127.0.1.$i" >> hosts.txt; done
```


## Username enum script usage
```
bash brute_timing_user.sh "target login uri"
```

### Example

![image](https://user-images.githubusercontent.com/86168235/126821805-7a4e7640-1368-40a1-950d-2e413be5d565.png)


## Password brute script usage
```
bash brute_timing_pass.sh "target login uri" "username"
```

### Example

![image](https://user-images.githubusercontent.com/86168235/126822014-c71bcd40-8e26-46c2-9c36-99d1ca65f4e1.png)
