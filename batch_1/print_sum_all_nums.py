#Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#input 10 numbers
total_sum = 0
for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    total_sum += number

#Print the sum of all the numbers.
print(total_sum)