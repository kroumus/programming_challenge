#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers

#input 10 numbers
initial = 0
for i in range(10):
    numbers = int(input(f"Enter Number {i+1}: "))
    if initial == 0:
        initial = numbers
    else:
        initial -= numbers

#print the result of the first number minus all of the remaining numbers
print(initial)

