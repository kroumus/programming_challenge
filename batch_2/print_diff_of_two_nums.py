#Create a program that ask user to input 2 numbers. Print the difference of the two numbers

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 2 numbers
num_list = []
for i in range(2):
    numbers = int(input(f"{PINK}Enter Number {i+1}: "))
    num_list.append(numbers)

#print the difference of the two numbers
difference = num_list[0] - num_list[1]
print(f"The difference of the two numbers is {difference}")