Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... userSalary = int(input("Enter the Salary \n"))
... 
... if(userSalary > 100000):
...     tax = (userSalary*0.10)
...     netSalary = userSalary - tax
...     print("Rs", tax, " tax 10% has been deducted from your salary \n")
...     print("Your net salary is ", netSalary)
... else:
...     tax = (userSalary * 0.05)
...     netSalary = userSalary - tax
...     print("Rs", tax, " tax 5% has been deducted from your salary \n")
...     print("Your net salary is ", netSalary)
... 
... 
SyntaxError: multiple statements found while compiling a single statement
