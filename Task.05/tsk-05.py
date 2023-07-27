Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... userName = input("Enter the name \n")
... userPassword = input("Enter the password \n")
... 
... name = "aliahmed"
... password = "ali12345"
... validateName = False
... validatePassword = False
... 
... if(len(name) == len(userName)):
...     for i in range(len(name)):
...         if(userName[i] == name[i]):
...             validateName = True
...             continue
...         elif (userName[i] != name[i]):
...             print("\nInvalid name credential")
...             validateName = False
...             break
... else:
...     print("Invalid name")
... 
... if(len(password) == len(userPassword)):
...     for i in range(len(password)):
...         if(userPassword[i] == password[i]):
...             validatePassword = True
...             continue
...         elif( userPassword[i] != password[i]):
...             print("\n Invalid Password")
...             validatePassword = False
...             break
... else:
...     print("Invalid Password")
... if(validateName and validatePassword):
...     print("\n Access Granted")
... else:
        print("Not granted")


