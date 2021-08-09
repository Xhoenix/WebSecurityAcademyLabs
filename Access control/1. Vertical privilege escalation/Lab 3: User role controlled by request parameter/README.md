Try to login with the provided credentials `wiener:peter` and intercept the login request. In Burp, edit the `Cookie` header of the login request(or **GET** request to `/my-account` page) and replace `Admin=false` with `Admin=true` and `Forward` the request. You'll be logged in with full admin rights. 

![image](https://user-images.githubusercontent.com/86168235/128717936-1904097e-43c2-4ce4-a4b1-ba4c8930a974.png)

Click on the `Admin panel` link and intercept the request. Replace the `Admin=` in the `Cookie` header in the same as you did above. You'll land on the Admin panel. Next, repeat the same method as above and delete the `carlos` user.
