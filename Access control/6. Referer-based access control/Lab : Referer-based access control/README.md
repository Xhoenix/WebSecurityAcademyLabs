Set the **Target Scope** and under **Sitemap** set a filter to *Show only in-scope items*. Turn Burp Proxy intercept **off**. Now login as the administrator user and visit the **Admin panel**. Click on `Upgrade user` and you'll see a **GET** request being made as follows:-

![image](https://user-images.githubusercontent.com/86168235/128723673-bd319691-d180-4979-ada2-97dc3c884414.png)

Take a note that the `Referer` header here contains the `/admin` url. Next, logout and login as the `wiener` user. Click on **My account** link and intercept the request with Burp and send it to repeater. On the repeater tab, change the `Referer` header to contain the `/admin` url and change the `/my-account` **GET** request url to as follows:-

![image](https://user-images.githubusercontent.com/86168235/128723800-72d0c72f-ad2d-4689-9936-ef7c19229b03.png)


Next, send the request and refresh the `/my-account` webpage you'll see that `wiener` has now access to the **Admin panel** in his account. Lab solved!!!
