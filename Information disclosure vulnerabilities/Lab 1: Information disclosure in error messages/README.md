First, in the lab click on `View details` of any product. Once on the product details page, change the `productId` parameter value in url bar to a **string** instead of a number and hit enter. You'll see the framework version number outputted alongwith the error message.

### Example

![image](https://user-images.githubusercontent.com/86168235/128642319-47380a2a-063a-448a-a95d-f422a6a97d60.png)


As the application was expecting an **number** as the value of `productId` parameter, providing it with a **string** made the app create an error.

