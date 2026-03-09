#Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

#input 2 numbers 
num_list = []
for i in range(2):
    numbers = float(input(f"Enter Number {i+1}: "))
    num_list.append(numbers)

#print the quotient of the two numbers without the decimal point
quotient = num_list[0] / num_list[1]
print(f"The quotient of the two numbers without the decimal point is {int(quotient)}")