# # Conditional

# if condition:
#     do this
# else :
#     do this

# Operators
# > Greater than
# < Less than
# >= Greater than equal to 
# <= Less than equal to
# == equal to 
# != Not equal to 

                                        ### experiment -1

# print("Welcome to roller coaster")
# height = (int(input("What is your height in cm ?")))
# bill = 0


# # if height >= 120 :
#     bill = 5
#     print("Your can enjoy the ride")
#     age = int(input("What is your age ?"))

#     if age <= 18 :
#         bill = 7
#         print('Please Pay 7$')
    
#     elif age >= 22:
#         bill = 12
#         print('Please Pay 12$')
    
#     else:
#         bill = 15
#         print('Please Pay 15$')
#     photo = input("Do you want a photo taken? Y  for yes or N for No ")

#     if photo == "Y":
#         print("Please pay $3 more")

#     bill += 3
    
#     print("SO your final bill is $", bill, "!")
    
# else:
    # print("Sorry ! Yoube have to grow taller to take this ride")


# # # #                           ### Modulo Operator ( % ) ### ( Remainder ))

# print(10%4)


                                        ### experiment - 2

# print("Welcome to Python pizza Deliveries!")
# size = input("What size pizza do you want? S for Small, M for Medium, or L for Large ")
# cheese = input("Do you want extra cheese? Y or N ")
# pepperoni = input("Do you want pepperoni? Y or N ")

# Small = 15
# Medium = 20
# Large = 25
# bill = 0 # starting bill
# cheese = 5
# pepperoni = 2

# if size == "S":
#   bill = 15
#   if pepperoni == "Y":
#     bill += 2
#   if cheese == "Y":
#     bill += 5
#   print("Your final bill is: $", bill)
# elif size == "M":
#   bill = 20
#   if pepperoni == "Y":
#     bill += 2
#     if cheese == "Y":
#       bill += 5
#       print("Your final bill is: $", bill)

# elif size == "L":
#   bill = 25
#   if pepperoni == "Y":  
#     bill += 2
#     if cheese == "Y":
#       bill += 5
#       print("Your final bill is: $", bill)
      



# print("Your final bill is: $", bill + cheese + pepperoni)

                    # Project --------------->>>>>>>>>>>>>>>>>>>>> 3
# Tresure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

left = "left"
wait = "wait"
red = "red"
yellow = "yellow"
blue = "blue"

print("welcome to treasure island")
print(input("you are at a crossroad, where do you want to go? Type 'left' or 'right' "))
if left == "left":
  print(input("you come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. "))
  if wait == "wait":
    print(input("you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? "))
    if red == "red":
      print("it's a room full of fire. Game Over.")
    elif yellow == "yellow":
      print("you found the treasure! You Win!")
    elif blue == "blue":
      print("you enter a room of beasts. Game Over.")
  else:
    print("you get attacked by an angry trout. Game Over.")
