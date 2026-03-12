#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#create a program that ask user to input a number, continue asking until the user input is invalid
inputted = []
while True:
    numbers = input("Enter a Number: ")
    inputted.append(numbers)
    if not numbers.isdigit():
        print("Invalid")
        break
#Display the lowest number
    lowest_number = min(numbers)
    print(lowest_number)
