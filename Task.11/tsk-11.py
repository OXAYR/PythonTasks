Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> total = int(input("Enter the total bill"))
... while(True):
...     print("Welcome to the shop\n"+
...             "Here is the menu for you\n"+
...           "1. Gold \n"+
...           "2. Silver \n"+
...           "3. Bronze \n"+
...           "4. No membership \n")
...     choice = input("Enter your current membership status \n")
...     match choice:
...         case '1':
...             print("20% discount has been given to you as you are a gold member")
...             if(total >= 1000):
...                 discount = (total * 0.25)
...                 netTotal = total - discount
...                 print("Additional 5% dicount has been provided as your bill is above 1000 \n")
...                 print("Your Net Total is after 25% discount ", netTotal)
...             else:
...                 discount = (total * 0.20)
...                 netTotal = total - discount
...                 print("Your Net Total is after 20% discount ", netTotal)
...             break
...         case '2':
...             print("15% discount has been given to you as you are a silver member")
...             if(total >= 1000):
...                 discount = (total * 0.20)
...                 netTotal = total - discount
...                 print("Additional 5% dicount has been provided as your bill is above 1000 \n")
...                 print("Your Net Total is after 20% discount ", netTotal)
...             else:
...                 discount = (total * 0.15)
...                 netTotal = total - discount
...                 print("Your Net Total is after 15% discount ", netTotal)
...             break
        case '3':
            print("10% discount has been given to you as you are a bronze member")
            if (total >= 1000):
                discount = (total * 0.15)
                netTotal = total - discount
                print("Additional 5% dicount has been provided as your bill is above 1000 \n")
                print("Your Net Total is after 15% discount ", netTotal)
            else:
                discount = (total * 0.10)
                netTotal = total - discount
                print("Your Net Total is after 10% discount ", netTotal)
            break
        case '4':
            if (total >= 1000):
                discount = (total * 0.05)
                netTotal = total - discount
                print("Additional 5% dicount has been provided as your bill is above 1000 \n")
                print("Your Net Total is after 5% discount ", netTotal)
            else:
                netTotal = total
                print("No discount has been provided to you as the bill is "
                      "less than 1000 and your are not a member")
                print("Your Net Total is ", netTotal)
            break
        case _:
            print("***************** Invalid input ******************** \n"
                  "Please Try again by entering the valid input \n")
            
SyntaxError: multiple statements found while compiling a single statement
