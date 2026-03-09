#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 2 numbers
nums_in_between = []
for i in range(2):
    numbers = int(input(f"{PINK}Enter Number {i+1}: "))
    nums_in_between.append(numbers)
        
#print all the numbers between the two numbers
if nums_in_between[0] < nums_in_between[1]:
    for i in range(nums_in_between[0] + 1, nums_in_between[1]):
        print(f"{PINK}", i, end=" ")
else:
    for i in range(nums_in_between[1] + 1, nums_in_between[0]):
        print(f"{PINK}", i, end=" ")