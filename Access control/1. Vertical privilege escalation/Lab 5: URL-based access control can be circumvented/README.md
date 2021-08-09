Trying to access **Admin panel** link on the home page results in an `Access denied` error. So, intercept the request with Burp and send it to repeater. Next, according to [OWASP](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema), we `Send a Request with an X-Original-Url Header Pointing to a Non-Existing Resource` and test whether it supports `X-Original-URL` header.

![image](https://user-images.githubusercontent.com/86168235/128718745-e38b94eb-3adf-4e74-a6aa-160516a6e25d.png)

So the `X-Original-URL` header is supported. Next, we try to access the admin page using this header. Reload the home page and intercept the request with Burp. Then add the `X-Original-URL` header. Example:-

![image](https://user-images.githubusercontent.com/86168235/128718830-9ecf4436-647e-4987-9a49-3a73e6dde3fd.png)

`Forward` the request and you'll land on the **Admin panel** page. Next, click on **Delete** link besides `carlos` user and intercept the request with Burp. Set the `X-Original-URL` to `/admin/delete` and the url query to `/?username=carlos` and `Forward` the request. Lab will be solved!!!

![image](https://user-images.githubusercontent.com/86168235/128718906-879b4d1e-70e0-479d-bca6-68623762cfde.png)
