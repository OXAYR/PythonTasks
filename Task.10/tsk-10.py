Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while(True):
...     print("Welcome to the restaurant \n"+
...             "Here is the menu for you\n"+
...           "1. Burger \n"+
...           "2. Pizza \n"+
...           "3. Drink \n")
...     choice = input("Enter your choice by entering the index number of thing you want from the menu \n")
... 
...     match choice:
...         case '1':
...             print("Your order of burger has been placed \n"
...                   "Thank you for using our service")
...             break
...         case '2':
...             print("Your order of pizza has been placed \n"
...                   "Thank you for using our service")
...             break
...         case '3':
...             print("Your order of drink has been placed \n"
...                   "Thank you for using our service")
...             break
...         case _:
...             print("***************** Invalid input ******************** \n"
...                   "Please Try again by entering the valid input \n")
