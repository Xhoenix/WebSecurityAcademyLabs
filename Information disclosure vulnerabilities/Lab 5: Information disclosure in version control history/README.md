First, we start off with a `Gobuster` directory scan.

### Gobuster

![image](https://user-images.githubusercontent.com/86168235/128643008-fce8dee4-b3d2-49eb-85f9-cd85adc8dbbd.png)

We see there is a `.git` folder indicating that there might be some version control data of past changes to the site available. So, lets check our concept by downloading the `.git` folder and its contents to our local filesystem using [GitTools](https://github.com/internetwache/GitTools).

![image](https://user-images.githubusercontent.com/86168235/128643056-028fef64-3b83-46ac-aa07-552cc69d66d5.png)

[GitTools](https://github.com/internetwache/GitTools) downloaded the `.git` folder for us.

![image](https://user-images.githubusercontent.com/86168235/128643090-c380d2ae-f968-4bc3-b615-4f04684450a1.png)

Next, lets do a `git diff` and see if we can find any valuable infomation.

![image](https://user-images.githubusercontent.com/86168235/128643121-375c7844-a48b-4af3-bf1f-e29988ff874a.png)

Looks like there is a `ADMIN_PASSWORD` environment variable. So, next lets check the `git log` to find all the **git commit logs** with changes to the `ADMIN_PASSWORD` variable. 


![image](https://user-images.githubusercontent.com/86168235/128643157-d121aa17-cf8c-413b-9322-8819363e7b11.png)

And so, we've the `administrator` password and are able to solve the lab. :)



