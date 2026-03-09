#Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 2 numbers
num_list = []
for i in range(2):
    numbers = int(input(f"{PINK}Enter Number {i+1}: "))
    num_list.append(numbers)

#print "Not Equal" when the numbers are not the same
if num_list[0] != num_list[1]:
    print("Not Equal")
else:
    print("Equal")