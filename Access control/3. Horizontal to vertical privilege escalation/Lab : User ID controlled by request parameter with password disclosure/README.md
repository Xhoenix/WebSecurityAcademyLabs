Login as the `wiener` user. Click on `My account` link. In the url bar change the `?id=wiener` to `?id=administrator` and hit enter.

![image](https://user-images.githubusercontent.com/86168235/128721098-ff494483-011e-4d42-9abc-244e1a3747f2.png)

On the administrator account page the password input box will be masked and we'll not be able to see the password directly. Right click on the `Password` input box and select `Inspect Element`. It'll open the firefox Inspector and you can see the **administrator** password in clear text. Next, logout and login as the **administrator** user and delete the `carlos` user from **Admin panel** to solve the lab!
