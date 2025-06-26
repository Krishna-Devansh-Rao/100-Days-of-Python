# # # # # Day 5 

# # # # # For LOOP 

# # # # # for item in list_of_item :
# # # #     #Do something to each item

# # # # fruits = [ 'Apple' , 'Banana' , 'Grapes']

# # # # for fruit in fruits:
# # # #     print(fruit)
# # # #     print(fruit + ' pie')
# # # #     print(fruits)


# # # # a = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # # # b = sum(a)

# # # # for b in a:
# # # #     print(b)

# # # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  
# # # 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  
# # # 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
# # # 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,  
# # # 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,  
# # # 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,  
# # # 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,  
# # # 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,  
# # # 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,  
# # # 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# # # print(sum(a))


# # # Range 
# # print(range(2 , 5))

# # for no in range( 1 , 12 , 5):
# #     print(no)


# # Fizzbuzz

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")    
#     else:
#         print(i)

# EXP - 5 

import random

print("Welcome to Password Generator")
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
symbols = ["!","@","#","$","%","^","&","*","(",")"]

a = int(input("how many letter you would like in your password ? "))

b = int(input(f"How many symbols you would like to add ? "))

c = int(input(f"How many no.s you would like to add ? "))

password = []

for char in range(0 , a):
    password.append(random.choice(letters))

for char in range(0 , b):
    password.append(random.choice(numbers))

for char in range(0 , c):
    password.append(random.choice(symbols))


print(password)
random.shuffle(password)
print(password)

passwords = ""
for char in password:
    passwords += char

print(f'Your password is : {password}')
