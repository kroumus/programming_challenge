#Create a program that ask user to input a number, continue asking until the user input is invalid. 
#Display the number with the most number of duplicate.

#input a number, continue asking until the user input is invalid.
inputted = []
while True:
    numbers = input(f"Enter a Number: ")
    if not numbers.isdigit():
        print("Invalid")
        break
    
    
    inputted.append(numbers)
    highest_duplicate = max(set(inputted), key=numbers.count)
