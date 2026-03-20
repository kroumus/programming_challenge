#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 10 numbers and list comrehension
numbers = [int(input(f"{PINK}Enter Number {i+1}: ")) for i in range(10)]

#diplay all numbers that don't have duplicate
no_duplicate = [n for n in numbers if numbers.count(n) == 1]
print(*no_duplicate)