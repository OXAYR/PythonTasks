Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> marks1 = int(input('Enter the marks of the first subject \n'))
... marks2 = int(input("Enter the marks of the second subject\n"))
... 
... if(marks1 <= 100 and marks2 <= 100):
...     avg = (marks1 + marks2)/2
...     if(avg >= 50):
...         print("Student has been passed with the average of ", avg)
...     else:
...         print("Student has been failed with the average of ", avg)
... else:
...     print("Invalid Input marks should be less than total marks which is 100 ")
...     
SyntaxError: multiple statements found while compiling a single statement
