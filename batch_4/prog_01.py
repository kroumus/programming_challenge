#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#input 10 numbers
duplicate = []
unique = []
numbers = [input(f"Enter Number {i+1}: ") for i in range(10)]

#Display all numbers that have duplicate
for n in numbers:
    if n in unique:
        if n not in duplicate:
            duplicate.append(n)
    else:
        unique.append(n)
print(*duplicate)