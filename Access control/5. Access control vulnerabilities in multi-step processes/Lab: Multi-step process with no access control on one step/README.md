Set the `Target Scope` in Burp to our target website and set a filter to *Show only in-scope items*. Turn Burp Proxy intercept **off**. Login as the Administrator user and go to the **Admin panel**. Click on `Upgrade user` and then click on **Yes** on the next step. Now go into Burp check the history in **Sitemap** under **Target** tab. You'll see a POST request to the `/admin-roles` page as follows:-

![image](https://user-images.githubusercontent.com/86168235/128722963-557ef485-dcbf-4d00-847c-fd916e9b9e57.png)

Take a note of this request and logout. Next, login as the `wiener` user, click on `My account` and intercept the request with Burp and send it to repeater. In the repeater tab, change the request method to **POST** and `/my-account` to `/admin-roles` then add `action=upgrade&confirmed=true&username=wiener`(as noted under the **Sitemap** tab) as the body. We just copied the same request as made by the administrator user but with the `wiener` user's session cookie. Next, send the request and the `wiener` user will have admin level access and the lab must be solved now!

