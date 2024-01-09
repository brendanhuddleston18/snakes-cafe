print("""\n**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears\n
***********************************
** What would you like to order? **
*********************************** \n""")

userOrder = []
userInput = input("""> """)
userOrder.append(userInput)
print(f"**{userOrder.count(userInput)} order of {userInput} has been added to your meal**")

while userInput != "quit":
  userInput = input("""> """)
  userOrder.append(userInput)
  # print(userOrder)
  if userOrder.count(userInput) == 1:
    print(f"**1 order of {userInput} has been added to your meal**")
  elif userOrder.count(userInput) > 1:
    print(f"**{userOrder.count(userInput)} orders of {userInput} has been added to your meal**")


  
