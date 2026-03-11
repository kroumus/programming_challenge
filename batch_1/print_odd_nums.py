#Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#input 10 numbers
odd_count = 0
for i in range(10):
    numbers = int(input(f"Enter number {i+1}: "))
    if numbers % 2 != 0:
        odd_count += 1 

#Print how many are odd numbers
print(odd_count)