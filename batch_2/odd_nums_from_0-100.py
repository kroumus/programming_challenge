#Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

for i in range(1, 101, 2):
    print(f"{PINK}",i, end=" ")