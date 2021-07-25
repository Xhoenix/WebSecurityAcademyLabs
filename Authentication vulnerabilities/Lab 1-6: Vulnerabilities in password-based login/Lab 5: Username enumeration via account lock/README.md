# Username enumeration via account lock

In this scenario we are not aware of a valid username. So, we take a list of usernames and use each username 5 times to login in order to create login attempt error if the username is valid. Note, you've to do your research with the login box to figure out the exact error messages. 

## Username enum Script usage
```
python3 account_lock_user.py
Enter target url: "target login uri"
```
### Example Screenshot

![image](https://user-images.githubusercontent.com/86168235/126832577-19d791db-eccc-4ab8-a8af-1367ab1a1c57.png)
![image](https://user-images.githubusercontent.com/86168235/126832646-7a82c80b-6f88-4d9c-ba2e-4b599d8172bd.png)

## Password brute Script usage
```
python3 account_lock_pass.py
Enter target url: "target login uri"
Enter target username: "target username"
```
### Example Screenshots
![image](https://user-images.githubusercontent.com/86168235/126833508-6631fa08-2128-41b2-9045-f00efbeceba7.png)
![image](https://user-images.githubusercontent.com/86168235/126833445-cf4a8456-ca3e-459a-84f9-6588726a55bf.png)

![image](https://user-images.githubusercontent.com/86168235/126833185-84bacc1e-5bfd-4f3c-8319-f7501ffd8e7b.png)



**Note**:- You've to wait for 1 minute after getting the password to login.
