#Create a program that ask user to input a number, continue asking until the user input is invalid. 
#Display "Unique" after input when the inputted number don't have duplicate. 
#Display "Duplicate" after input when the inputted number have duplicate.

#input a number, continue asking until the user input is invalid.
inputted = []
while True:
    numbers = input("Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid")
#Display "Duplicate" after input when the inputted number have duplicate.    
    if numbers in inputted:
        print("Duplicate")
#Display "Unique" after input when the inputted number don't have duplicate.     
    else:
        print("Unique")
        inputted.append(numbers)

   