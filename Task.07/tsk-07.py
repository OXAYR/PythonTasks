Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... 
... year=int(input("Enter year to be checked:"))
... if(year%4==0 and year%100!=0 or year%400==0):
...     print("The year is a leap year!")
... else:
        print("This year is not a leap year!")
