#Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

#input 2 numbers
num_1 = input("Enter 1st Number: ")
num_2 = input("Enter 2nd Number: ")

#Print "Equal" when the numbers are the same
if num_1 > num_2:
    print((f"{num_1} is bigger!"))
elif num_1 < num_2:
    print((f"{num_2} is bigger!"))
else:
    print("Equal")