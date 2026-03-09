#Create a program that ask user to input 10 numbers. Print how many are even numbers

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 10 numbers
even_numbers = 0
for i in range(10):
    numbers = int(input(f"{PINK}Enter Number {i+1}: "))
    if numbers % 2 == 0:
        even_numbers += 1

#print even numbers
print(even_numbers)
