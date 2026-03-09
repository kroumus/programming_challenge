#Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 2 number
num_list = []
for i in range(2):
    numbers = int(input(f"{PINK}Enter Number {i+1}: "))
    num_list.append(numbers)

#print the remainder
remainder = num_list[0] % num_list[1]
print(remainder)