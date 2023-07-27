Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  x = float(input("Enter the x-coordinate: "))
...  y = float(input("Enter the y-coordinate: "))
... 
...  if x == 0 and y <= 30:
...      print("The aircraft is in quadrant 1.")
...  elif x == 0 and y >= 30 and y <= 90:
...      print("The aircraft is in quadrant 2.")
...  elif x > 0 and y >= 90 and y <= 120:
...      print("The aircraft is in quadrant 3.")
...  elif x == 180 and y >= 120 and y <= 180:
...      print("The aircraft is in quadrant 4.")
...  elif x == 180 and y >= 180 and y <= 210 :
...      print("The aircraft is in quadrant 5.")
...  elif x == 180 and y >= 210 and y <= 270:
...      print("The aircraft is in quadrant 6.")
...  elif x == 0 and y >= 270 and y <= 300:
...      print("The aircraft is in quadrant 7.")
...  elif x == 0 and y >= 300 and y <= 360:
...      print("The aircraft is in quadrant 8.")
...  elif y == 0 and x != 0:
...      print("The aircraft is on the y-axis.")
...  elif x == 0 and y != 0:
...      print("The aircraft is on the x-axis.")
...  else:
...      print("The aircraft is at the origin.")
...      
SyntaxError: unexpected indent
>>> 
>>> 
