#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input a number, continue asking until the user input is invalid.
inputted = []
while True:
    numbers = input(f"{PINK}Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid")
        break

#Display the lowest number
    inputted.append(numbers)
    set()