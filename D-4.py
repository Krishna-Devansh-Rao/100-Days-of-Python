# # # Day - 4

# # # Randomisastion
# # # 

# # import random
# # import my_module

# # # a= random.randint( 1 , 20)
# # # print(a)
# # # print(my_module.my_fav)

# # # b =  random_number_0_to_10 = random.random() *100
# # # print(b)

# # # c = random.uniform(3,15)

# # # print(c)

# # # H_T = random.randint(0 ,1)
# # # if H_T == 0:
# # #     print("Heads")
# # # else :
# # #     print("Tails")

# # # Lists

# # Fruits = ["Apple", " Grapes" , "Mango","Banana", "Cherry"]
# # # print(Fruits[4])

# # # Fruits.append("Orange")

# # # Fruits.append("pineapple")

# # # Fruits.extend("Dragon Fruit") # ['Cherry', 'D', 'r', 'a', 'g', 'o', 'n', ' ', 'F', 'r', 'u', 'i', 't']

# # Fruits.remove('Mango')




# # print(Fruits)
# import random
# Fruits = ["Apple", " Grapes" , "Mango","Banana", "Cherry"]
# print(random.choice(Fruits))

# a = random.randint(0,4)
# print(Fruits[a])


# #Rock paper game 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
