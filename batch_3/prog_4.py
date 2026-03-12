#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#create a program that ask user to input a number, continue asking until the user input is invalid
inputted = []
while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid")
