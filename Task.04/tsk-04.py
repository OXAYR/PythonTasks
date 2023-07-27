Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... get = input("Enter an alphabet to check for vowel or consonent ")
... lst = 'aeiou'
... lst2 = 'bcdszxvnmlkjhgfdsqwrtyp'
... 
... 
... for i in range(len(lst)):
...     if(get == lst[i]):
...         print("\nIt is a vowel")
...         break
...     else:
...         continue
... 
... for i in range(len(lst2)):
...     if(get == lst2[i]):
...         print("\nIt is a consonent")
...         break
...     else:
...         continue
... 
SyntaxError: multiple statements found while compiling a single statement
