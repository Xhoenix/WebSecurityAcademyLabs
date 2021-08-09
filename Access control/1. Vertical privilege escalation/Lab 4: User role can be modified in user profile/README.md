Login with the credentials provided(wiener:peter). Enter a random email in the email box and click `Update email`. Intercept the request with Burp and send it to repeater. In repeater send the request and in the response you'll see that there is a "roleid" key with value "1". 

![image](https://user-images.githubusercontent.com/86168235/128718268-b810bd8a-c254-4dcc-99a8-e6fa40bdbc2d.png)

Next edit the json in the request and add `"roleid":2` and send the request. You'll see the **roleid** changed in response.

![image](https://user-images.githubusercontent.com/86168235/128718416-09503984-bb26-4c0d-a6d9-7daee0e00fae.png)

Now, in the browser refresh the `my-account` page and you'll see that you've access to a new link called **Admin panel**. Click on it and delete the carlos user.
