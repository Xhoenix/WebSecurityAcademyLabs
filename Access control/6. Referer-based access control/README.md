# Referer-based access control
Set the **Target Scope** and under **Sitemap** set a filter to *Show only in-scope items*. Turn Burp Proxy intercept **off**. Now login as the administrator user and visit the **Admin panel**. Click on `Upgrade user` and you'll see a **GET** request being made as follows:-

![image](https://user-images.githubusercontent.com/86168235/228804287-da9e78a1-1ada-4fc6-b9c1-52a6943b8a27.png)


Take a note that the `Referer` header here contains the `/admin` url. Next, logout and login as the `wiener` user. Click on **My account** link and intercept the request with Burp and send it to repeater. On the repeater tab, change the `Referer` header to contain the `/admin` url and the `/my-account` **GET** request url to as follows:-

![image](https://user-images.githubusercontent.com/86168235/228804411-fd8a1f5a-c59c-4cda-b455-8d7812427a17.png)

Next, send the request and refresh the `/my-account` webpage you'll see that `wiener` has now access to the **Admin panel** in his account. Lab solved!!!
