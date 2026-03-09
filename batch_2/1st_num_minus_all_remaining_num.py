#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#input 10 numbers
initial = 0
for i in range(10):
    numbers = int(input(f"{PINK}Enter Number {i+1}: "))
    if initial == 0:
        initial = numbers
    else:
        initial -= numbers

#print the result of the first number minus all of the remaining numbers
print(initial)

