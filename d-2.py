# # # # # #                           ### Day -2 ###

# # # # # # # print("Hello World"[-2]) #subscripting

# # # # # # # string
# # # # # # # print("123" + "345")

# # # # # # # # Integer = whole numbers
# # # # # # # print(123 + 345)

# # # # # # # #Large Integers
# # # # # # # print(123_456_789)

# # # # # # # # float = FloatingPointNumber
# # # # # # # float = 3.14159
# # # # # # # print(float)

# # # # # # # # Boolen
# # # # # # # print(True)
# # # # # # # print(False)

# # # # # # print(type("Hello World")) #<class 'str'>
# # # # # # print(type(123)) #<class 'int'>
# # # # # # print(type(3.14159)) #<class 'float'>
# # # # # # print(type(True)) #<class 'bool'>

# # # # # name_of_the_user = input("Enter your name: \n ")
# # # # # print(len(name_of_the_user))
# # # # # lenght_of_the_name = len(name_of_the_user)

# # # # # print(type("No of letters in your name is: " ))
# # # # # print(type( lenght_of_the_name))


# # # # print("My age : " + str(18))
# # # # a = print(6 / 3 )
# # # # b = print(6 // 3 )

# # # # print(type( 6 / 3))  #integer ke sath integer ka division karne par float aata hai
# # # # print(type( 6 // 3))  #integer ke sath integer ka division karne par integer hi aata hai
# # # # print(2**4) #Power mai ** ka use hota hai

# # # bmi = 75 / 1.65 ** 2
# # # print(bmi)
# # # print(int(bmi))
# # # print(type(bmi))
# # # print(round(bmi))
# # # print(round(bmi, 3))



# #                                 #f-string

# # score = 0

# # score += 1

# # print(score)

# # print((" Your score is : ") + str(score))

# score = 0 
# height = 1.8
# is_winning = True

# print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}") 

                                ###Project 2###

print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

