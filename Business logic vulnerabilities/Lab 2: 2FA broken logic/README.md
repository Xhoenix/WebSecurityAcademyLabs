# Enumeration
First set the `Target Scope` on Burp to the url of the lab. Next login as `wiener` user and you'll land on a page called `login2` asking for a security code.
![image](https://user-images.githubusercontent.com/86168235/129616459-47c957b9-f69b-42c7-937f-4ad104e81033.png)

Go to the `Email client` and get the code and submit it here. You'll be logged in.

&nbsp;

Next, on Burp Target Sitemap you'll see all the requests as follows:-
![image](https://user-images.githubusercontent.com/86168235/129616615-d9c546e0-6ca1-4d4e-9d7c-6c6de7431487.png)

Here two requests are of interest to us. 

## One
There is a **GET** request to the `/login2` after a **POST** request to `/login` .

![image](https://user-images.githubusercontent.com/86168235/129616759-83dc6dc0-36fe-4727-ab25-99ecc2c08df2.png)

In this request, the `verify` parameter in `Cookie` header is vulnerable as it is used to determine which user is accessing the `/login2` page. We can use this **GET** request to generate 2FA codes for any user by changing the `verify` parameter to a different valid username.

&nbsp;

### Example
Send the **GET** request to *repeater* and on the repeater tab change the `verify` parameter value to `carlos` and send the request. You'll see the **security code** page in response.

![image](https://user-images.githubusercontent.com/86168235/129617061-3f551428-b5fc-40b7-8357-1f95b9d02125.png)
This means we can generate 2FA codes for `carlos` user without logging in with valid credentials. 

&nbsp;
&nbsp;

## Two
There is a **POST** request to `/login2` where again the `verify` parameter in `Cookie` header is used to check for a user logging in.

![image](https://user-images.githubusercontent.com/86168235/129617995-65718247-8b30-461c-b95e-3e914cb265b6.png)

In the body of this request we can see our 2FA code is being passed through the `mfa-code` parameter to log us in. As we can generate 2FA codes for any random user, we can use this **POST** request to `/login2` to bruteforce the 2FA code of the user by setting the `verify` cookie parameter to user's username.

![image](https://user-images.githubusercontent.com/86168235/129618180-776e3fd9-2695-4002-b785-a697977a9348.png)


&nbsp;

&nbsp;

&nbsp;

&nbsp;



# Exploitation

I have written a small python script to bruteforce `carlos` user's 2FA code and give us his session cookie once the correct pin is found. We can then use this session cookie to login as `carlos`.

## What the script does
The script first makes a **GET** request to `/login2` as the `carlos` user by setting the `Cookie` header to `"verify": "carlos"`, which in turn generates a 2FA code for `carlos` user.

![image](https://user-images.githubusercontent.com/86168235/129620419-bd75458a-d18f-4411-9bbd-cf3458a0283a.png)

Next, it makes **POST** requests to `/login2` to bruteforce the 2FA code using **multiprocessing** and gets the session cookie for us.

**Note**:- I've uploaded a file with 9999 2FA codes. You can use it or generate one using this command:- 
```for i in {0001..9999}; do echo "$i" >> top_9999.txt; done```. 
&nbsp;

Also, I've set the `pool` to `mp.Pool(40)` as I was able to solve the lab in 14 *seconds* by setting it to **50**. You're free to change this value as you wish, but you do so at your own risk. 

### Usage

```
python3 2fa_broken_logic.py
Enter target url: "Lab homepage URL"
```
#### Example
First, run the script as follows.

![image](https://user-images.githubusercontent.com/86168235/129619225-b2e69e38-ca85-4da5-b27e-9878a92075e9.png)

&nbsp;


It'll give you the session cookie once complete.

![image](https://user-images.githubusercontent.com/86168235/129619881-4b76b174-28f2-4d8d-af3b-6dd7f47d3583.png)

&nbsp;

Next, open up `Cookie Editor` in browser and paste the cookie and save it.

![image](https://user-images.githubusercontent.com/86168235/129619992-f6844b69-3d15-46a8-8632-635375cc5f97.png)

&nbsp;
Next, change the url in url bar to the `my-account` page and hit **enter**

![image](https://user-images.githubusercontent.com/86168235/129620058-ea15fd20-86d7-4843-9f5f-d6d6295f0d6c.png)

&nbsp;

You'll have access to the account page of `carlos` user. Happy hacking!

![image](https://user-images.githubusercontent.com/86168235/129620133-f99f10a3-7f88-418c-aa2f-7e4f41d6885f.png)

