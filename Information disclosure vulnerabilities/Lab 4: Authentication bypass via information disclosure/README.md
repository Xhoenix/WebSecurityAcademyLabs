First run a `gobuster` scan to determine the directory structure.

### Gobuster

![image](https://user-images.githubusercontent.com/86168235/128642568-83a0cd35-92dc-48d9-ad27-d762caa9ab1e.png)


We see that there is an `admin` page. Trying to access it gives us the message:- `Admin interface only available to local users`.

![image](https://user-images.githubusercontent.com/86168235/128642612-6bd6c867-1ecd-4055-a4f7-c0b5df0abc3c.png)


**Next**, running a **nikto** scan shows us the availability of the HTTP `TRACE` method.

![image](https://user-images.githubusercontent.com/86168235/128642637-6100b534-863a-4b01-8fb9-1b5875b5c75f.png)


As we know, a **HTTP TRACE** request returns the full HTTP request back, we can do a **HTTP TRACE** request to the `admin` page and see what headers we are missing in our **GET** request to bypass the access policy.

![image](https://user-images.githubusercontent.com/86168235/128642669-3a79b55d-a6af-4113-ac9f-8f999c80c550.png)

Next, refresh the **Admin Interface** page and intercept the request with Burp Proxy. Send the request to repeater and in the repeater tab change the **GET** method to **TRACE** and send the request.

![image](https://user-images.githubusercontent.com/86168235/128642700-10784102-ba3f-4321-8479-794870e21fba.png)

We see that the **TRACE** request returns the full HTTP request alongwith the custom header `X-Custom-IP-Authorization:` needed to access the Admin Interface page.

So, next reload the page again and intercept the request with Burp. Then, add the `X-Custom-IP-Authorization:` header with **127.0.0.1**(or **localhost**) as its value and then forward the request.

![image](https://user-images.githubusercontent.com/86168235/128642760-9b305930-12a7-4336-ab48-6fd45037698e.png)

The result is we're able to access the Admin Interface.

![image](https://user-images.githubusercontent.com/86168235/128642777-4d3423eb-b408-4f19-b73b-88af805e4721.png)

Finally, click on the `Delete` button beside user **carlos**, intercept the request and add the custom header as before and forward the request. The lab is solved. :)

## Optional

I've added a simple python script, running which will solve the lab for you. 

### Usage

![image](https://user-images.githubusercontent.com/86168235/128642815-317c021b-9b25-47db-b737-862ea1a57f0b.png)




