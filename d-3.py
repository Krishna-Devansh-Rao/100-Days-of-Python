# # # # # # # # Conditions 

# # # #                             ### if/else ###

# # # # # # # if condition: 
# # # # # # #   do this
# # # # # # # else condition:
# # # # # # #   do this

# # # #                             ### experiment -1

# # # # # print("Welcome to the rollercoaster!")
# # # # # height = int(input("what is your height in cm? "))
# # # # # if height >= 120:
# # # # #   print("You can ride the rollercoaster!")
# # # # # else  :
# # # # #   print("Sorry, you have to grow taller before you can ride.")


# # # #                           ### Modulo Operator ( % ) ### ( Remainder ))

# # # # # # # #  Modulo Operator ( % ) ###

# # # # # 12 % 2 == 0
# # # # # print(28 % 13 ) 

# # # weight = 85
# # # height = 1.85

# # # bmi = weight / (height ** 2)

# # # # 🚨 Do not modify the values above
# # # # Write your code below 👇

# # # # if bmi >= 18.5 :
# # # #     print("underweight")

# # # # elif bmi >= 18.5 :
# # # #     print("normal weight")

# # # # else :
# # # #     print("overweight") 

# # # if bmi >= 25:
# # #     print("overweight")
# # # elif bmi >= 18.5:
# # #     print("normal weight")
# # # else:
# # #     print("underweight")



# # print("Welcome to the rollercoaster!")
# # height = int(input("what is your height in cm? "))
# # bill = 0
# # if height >= 120:
# #   print("You can ride the rollercoaster!")
# #   age = int(input("what is your age? "))
# #   if age < 12:
# #     print("Please pay $5")
# #     bill = 5
# #   elif age <= 18:
# #     print("Please pay $7")
# #     bill = 7
# #   else:
# #     print("Please pay $12")
# #     bill = 12

# #   photo = input("Do you want a photo taken? Y  for yes or N for No ")
# #   if photo == "Y":
# #     print("Please pay $3 more")

# #     bill += 3
    
# #     print("SO your final bill is $", bill, "!")
    
   
  
    
# # else  :
# #   print("Sorry, you have to grow taller before you can ride.")

#                         ###Experiment -2 ###

# from typing import TYPE_CHECKING


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


                      





                        ### Logical Operators ###


                      #Project 3 - Treasure Island






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
