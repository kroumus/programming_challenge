#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#input 10 numbers with list comprehension
numbers = [int(input(f"Enter Number {i+1}: ")) for i in range(10)]