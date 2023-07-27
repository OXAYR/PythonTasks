Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>inpt1 = int(input('Enter the first digit you wanna compare\n'))
... inpt2 = int(input("Enter the second digit you wanna compare\n"))
... inpt3 = int(input("Enter the third digit you wanna compare\n"))
... 
... if(inpt1 == inpt2 and inpt2 == inpt3):
...     print("All number are same \n")
... elif(inpt1 == inpt2):
...     print(" input 1 AND  input 2 are equal =", inpt1, "=", inpt2)
... elif(inpt1 == inpt3):
...     print(" input 1 AND input 3 are equal =", inpt1, "=", inpt3)
... elif(inpt2 == inpt3):
...     print(" input 2 AND input 3 are equal =", inpt2, "=", inpt3)
... else:
...     print("All numbers are different \n")
...     
SyntaxError: multiple statements found while compiling a single statement



