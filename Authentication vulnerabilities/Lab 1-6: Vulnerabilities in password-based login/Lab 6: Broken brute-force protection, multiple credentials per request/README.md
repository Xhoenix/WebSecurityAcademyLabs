# Broken brute-force protection, multiple credentials per request

This lab was the most fun one for me in this series. I wanted to name this script the `2_seconds_exploit.py`🤣, but decided not to. Even though this exploit script is pretty simple, I'd to dig into the requests module which helped me learn a lot of other advanced stuff about `requests` itself. 
**Note**, running this script will automatically solve the lab challenge, but to achieve the actual goal, i.e, login as the victim, we've to do session hijacking with the session cookie of the user. Running this script will provide you with the user's session cookie.🙃 You've to login using it.🙂 

## Script usage

```
python3 single_request_brute.py
Enter target url: "target login url"
```

### Example
#### First get the user's `session` cookie by running the script
![image](https://user-images.githubusercontent.com/86168235/126836420-aca82a23-9fd8-4ce0-9e12-aabb26f888f6.png)

#### Next, open up `Cookie Editor` in the browser and paste the cookie into it and save it.
![image](https://user-images.githubusercontent.com/86168235/126837096-f47abcf7-6c5e-44ca-b0a9-2f5fc2919b27.png)


- - -


#### Then, edit the url in url bar and change the `login` to `my-account` and hit enter and voila!! 😎

![image](https://user-images.githubusercontent.com/86168235/126837658-11917860-ecbc-449c-a658-dbe7556f515a.png)

- - -

![image](https://user-images.githubusercontent.com/86168235/126837705-a90a9261-33e0-4ad7-846d-6a226639072c.png)




