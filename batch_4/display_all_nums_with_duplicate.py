#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 10 numbers
duplicate = []
unique = []
numbers = [input(f"{PINK}Enter Number {i+1}: ") for i in range(10)]

#Display all numbers that have duplicate
for n in numbers:
    if n in unique:
        if n not in duplicate:
            duplicate.append(n)
    else:
        unique.append(n)
print(*duplicate)