# # Funtion with input

# # def greet():
# #     print("Hello")
# #     print("World")
# #     print("This is Krishna Devansh Rao")
# # greet()

# # def greet_with_name(name):
# #     print(f"Hey this is {name}")
# #     print(f"I am {name}")

# # greet_with_name("Krishna")

# # age = int(input("What is your current age ?"))
# # left = 90 - age 
# # weeks = left * 52

# # def life_in_weeks(age):
# #     print("If we Live 90 Years")
# #     print(f"The no of weeks left in our life is {weeks}")
    
# # life_in_weeks(age)

# # def greet(name , location , number):
# #     print(f"Hey this is {name}")
# #     print(f"I live in {location}")
# #     print(f"My no is {number}")

# # greet("Krishna" , "Raipur"  , 8103889188)

# def love_calculator(name1, name2):
#     # Convert names to lowercase and combine
#     combined_names = (name1 + name2).lower()

#     # Count the letters in "TRUE"
#     true_score = 0
#     for char in "true":
#         true_score += combined_names.count(char)

#     # Count the letters in "LOVE"
#     love_score = 0
#     for char in "love":
#         love_score += combined_names.count(char)

#     # Combine the scores into a single number
#     love_percentage = int(str(true_score) + str(love_score))

#     # Interpretation
#     print(f"\nLove score for {name1} ❤️ {name2} is: {love_percentage}%")
#     if love_percentage > 80:
#         print("You are a perfect match! 💘")
#     elif 50 <= love_percentage <= 80:
#         print("There's definitely something special! 😊")
#     else:
#         print("Hmm... maybe just friends? 😅")

# # Example usage
# your_name = input("Enter your name: ")
# partner_name = input("Enter their name: ")

# love_calculator(your_name, partner_name)



from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

run = True
while run:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift = shift % shift == 0

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
  if choice == 'no':
    run = False
    print("Goodbye.")
