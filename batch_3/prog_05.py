#Create a program that ask user to input a number, continue asking until the user input is invalid.
#Display the number from lowest to highest. Clue: sort() function

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input a number, continue asking until the user input is invalid.
inputted = []
while True:
    numbers = input(f"{PINK}Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid")
        break

