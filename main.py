# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("\nEasy Level")
pw = ""
for n in range(0, nr_letters):
    pw += letters[random.randint(0, len(letters) - 1)]
for n in range(0, nr_symbols):
    pw += symbols[random.randint(0, len(symbols) - 1)]
for n in range(0, nr_numbers):
    pw += numbers[random.randint(0, len(numbers) - 1)]
print(pw)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("\nHard Level v1")
pw1_list = []
pw1 = ""
for n in range(0, nr_letters):
    pw1_list.append(letters[random.randint(0, len(letters) - 1)])
for n in range(0, nr_symbols):
    pw1_list.append(symbols[random.randint(0, len(symbols) - 1)])
for n in range(0, nr_numbers):
    pw1_list.append(numbers[random.randint(0, len(numbers) - 1)])
for n in range(0, len(pw1_list)):
    index = random.randint(0, len(pw1_list) - 1)
    pw1 += pw1_list[index]
    pw1_list.pop(index)
print(pw1)

print("\nHard Level v2")
pw2_list = []
pw2 = ""
for n in range(0, nr_letters):
    pw2_list.append(letters[random.randint(0, len(letters) - 1)])
for n in range(0, nr_symbols):
    pw2_list.append(symbols[random.randint(0, len(symbols) - 1)])
for n in range(0, nr_numbers):
    pw2_list.append(numbers[random.randint(0, len(numbers) - 1)])
random.shuffle(pw2_list)
for char in pw2_list:
    pw2 += char
print(pw2)
