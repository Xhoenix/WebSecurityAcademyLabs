First run `gobuster` scan to determine the directory structure. 

### Gobuster

![image](https://user-images.githubusercontent.com/86168235/128642398-9f6ac1ff-6292-4b03-b198-5b290b41bdf6.png)

The `cgi-bin` path looks interesting and is also accessible(**Status: 200**). Visting it lands us on a page like this:-

![image](https://user-images.githubusercontent.com/86168235/128642436-14861b63-0d61-4408-a75f-ca4285688bf9.png)


Visiting the `phpinfo` page you'll find the `SECRET_KEY` environment variable.
