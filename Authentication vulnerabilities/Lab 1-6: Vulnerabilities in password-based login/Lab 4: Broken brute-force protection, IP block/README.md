# Broken brute-force protection, IP block

In this scenario our IP is blocked if we make three incorrect attempts. But, if we make a valid login on our third request providing valid creds, then we can reset the counter which keeps track of number of incorrect attempts.
I've made a script that will try to provide passwords from a list for first two attempts and then provide valid username and password every third attempt so that our IP never gets blocked.


## Script usage
```
python3 flawed_brute.py
Enter target url: "target login uri"
Enter victim's username: {username}
```

### Example Screenshots
![image](https://user-images.githubusercontent.com/86168235/126830156-3e52f52c-e463-4e03-9070-6c082d600861.png)
![image](https://user-images.githubusercontent.com/86168235/126830520-0c66f703-1253-4a3f-aca8-0fad524bb992.png)

