On the homepage, click on `Live chat`. After doing some chat(if you want to), click on `View transcript` and intercept the request with Burp. After some testing, you'll see that the transcript files that are getting downloaded have a incrementing number as their **filename**. After intercepting the request, change the **filename** to `1.txt` in each subsequent request and forward them. You'll be able to download the file `1.txt`. View its contents and you'll find the password of the `carlos` user. Login to solve the challenge.


![image](https://user-images.githubusercontent.com/86168235/128722435-3ab69792-ff40-4509-8ba3-5a90ef4290fb.png)
