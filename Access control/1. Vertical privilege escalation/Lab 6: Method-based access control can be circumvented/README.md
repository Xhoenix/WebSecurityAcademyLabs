Login as administrator and visit the **Admin panel**. Try to downgrade user `carlos` and intercept the request. You'll see that there is a **POST** request to `/admin-roles` and with the body `username=carlos&action=downgrade`. Take a note of this.

Next, logout and login as the `wiener` user. Then on the `my-account` page try to refresh the webpage and intercept the request with Burp. Change the `/my-account` to `/admin-roles?username=wiener&action=upgrade`. Here, the HTTP method is actually **GET** instead of **POST** like it was when we are trying to downgrade the `carlos` user. 

![image](https://user-images.githubusercontent.com/86168235/128719553-fdab4096-4dc4-40a7-a65e-5673dad36e95.png)

Sending the request will solve the lab challenge and upgrade the wiener user to a administrator.

![image](https://user-images.githubusercontent.com/86168235/128719608-eb2bb51b-f11b-4c0e-aaed-19af5adea659.png)

