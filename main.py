# Project 5
# Password Generator
from random import choice, shuffle

# greet user
print("Welcome to PyPassword Generator.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# get number of letters
number_of_letters = int(input("How many letters would you like to have in your password?\n"))

# get number of integers
number_of_integers = int(input("How many numbers would you like to have in your password?\n"))

# get number of symbols
number_of_symbols = int(input("How many symbols would you like to have in your password?\n"))

# empty password list
password_list = []

# generate random letters, numbers and symbols
letters_list = [choice(letters) for letter in range(number_of_letters)]
numbers_list = [choice(numbers) for number in range(number_of_integers)]
symbols_list = [choice(symbols) for symbol in range(number_of_symbols)]

# combine all lists from above
password_list.extend(letters_list)
password_list.extend(numbers_list)
password_list.extend(symbols_list)

# shuffle the password list
shuffle(password_list)
password = "".join(password_list)

# print password
print(f"Here is your super strong password: {password}")
