#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#input 10 numbers with list comprehension
numbers = [int(input(f"Enter Number {i+1}: ")) for i in range(10)]

#Display all numbers. For numbers with duplicate, display only the first entry using fromkeys() function I learned from gemini ai
order_by_insertion = list(dict.fromkeys(numbers))
print(*order_by_insertion)