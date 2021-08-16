This lab can be solved in two different ways. While adding an item to cart we can modify the **POST** request body and change the `productId` parameter to that of another costlier product or we can reduce the value in the `price` parameter to a lesser value, which'll help us purchasing the product for a lesser price.

## Method 1
First, login as the `wiener` user and go to the home page. There, click on `View details` of the **Lightweight "l33t" Leather Jacket**. Next, turn Burp Proxy Intercept **on**. On the next page, click on "`Add to cart`". In Burp you'll see a **POST** request like this:-
![image](https://user-images.githubusercontent.com/86168235/129615254-f9ec3e7b-b719-4c19-88ba-a4b8fec47572.png)

Modify the `price` parameter to a value of your liking and `Forward` the request. Next go to cart and you'll see the price of the "**Lightweight "l33t" Leather Jacket**" will be changed to the price you set in the earlier step. Place the order and the lab will be solved.

![image](https://user-images.githubusercontent.com/86168235/129615322-12be2eb6-c5bb-4384-8f51-fa4996466338.png)

&nbsp;
&nbsp;
&nbsp;

## Method 2
First, login as the `wiener` user and go to the home page. There, click on `View details` of any product with value less than $100(Portswigger didn't give us more money🙃).  Next, turn Burp Proxy Intercept **on**. On the next page, click on "`Add to cart`". In Burp you'll see a **POST** request like this:-
![image](https://user-images.githubusercontent.com/86168235/129615399-05a10949-6f02-430d-8780-cedb068ef965.png)

Modify the `productId` value and set it to `1`(id of the leather jacket) and send the request. Next go to cart and you'll see the "**Lightweight "l33t" Leather Jacket**" added to your cart instead of the original item. The price of the **Lightweight "l33t" Leather Jacket** must be the price of the original item and not $1337. Place the order and the lab will be solved.

![image](https://user-images.githubusercontent.com/86168235/129615478-c79a4674-67cc-46e5-9eeb-41be8004cea4.png)
