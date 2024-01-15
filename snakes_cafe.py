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

while True:
  userInput = input("""> """)
  
  if userInput == "quit":
    break

  userOrder.append(userInput)
  if userOrder.count(userInput) == 1:
    print(f"**1 order of {userInput} has been added to your meal**")
  elif userOrder.count(userInput) > 1:
    print(f"**{userOrder.count(userInput)} orders of {userInput} has been added to your meal**")


  
