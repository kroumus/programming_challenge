#Create a program that ask user to input a number, continue asking until the user input is invalid. 
#Display "Unique" after input when the inputted number don't have duplicate. 
#Display "Duplicate" after input when the inputted number have duplicate.

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input a number, continue asking until the user input is invalid.
inputted = []
while True:
    numbers = input(f"{PINK}Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid")
        break
#Display "Duplicate" after input when the inputted number have duplicate.    
    if numbers in inputted:
        print("Duplicate") 
#Display "Unique" after input when the inputted number don't have duplicate.     
    else:
        print("Unique")
        inputted.append(numbers)