#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

choices = [0, 1, 2]
pwd = []

while len(choices) > 0:
    
    letter_or_number_or_symbol = random.choice(choices)
    
    #print(choices,' ', letter_or_number_or_symbol)

    if letter_or_number_or_symbol == 0 and nr_letters > 0:
        nr_letters -= 1
        pwd.append(letters[random.randint(0, len(letters) - 1)])
    elif letter_or_number_or_symbol == 0 and nr_letters == 0:
        #print(choices)
        choices.remove(0)
        
    if letter_or_number_or_symbol == 1 and nr_numbers > 0:
        nr_numbers -= 1
        pwd.append(numbers[random.randint(0, len(numbers) - 1)])
    elif letter_or_number_or_symbol == 1 and nr_numbers == 0:
        #print(choices)
        choices.remove(1)
        
    if letter_or_number_or_symbol == 2 and nr_symbols > 0:
        nr_symbols -= 1
        pwd.append(symbols[random.randint(0, len(symbols) - 1)])
    elif letter_or_number_or_symbol == 2 and nr_symbols == 0:
        #print(choices)
        choices.remove(2)
    

print(''.join(pwd))


    