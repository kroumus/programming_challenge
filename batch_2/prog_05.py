#Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number

#input 2 numbers
num_list = []
for i in range(2):
    numbers = float(input(f"Enter Number {i+1}: "))
    num_list.append(numbers)

#print the remainder when the first number is divided by the second number
remainder = num_list[0] % num_list[1]
print(remainder)