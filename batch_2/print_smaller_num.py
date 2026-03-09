#Create a program that ask user to input 2 numbers. Print the smaller number

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 2 numbers
smaller_num = []
for i in range(2):
    number = int(input(f"{PINK}Enter Number {i+1}: "))
    smaller_num.append(number)

#print the smallest number
if smaller_num[0] < smaller_num[1]:
    print(f"{smaller_num[0]} is smaller")
else:
    print(f"{smaller_num[1]} is smaller")