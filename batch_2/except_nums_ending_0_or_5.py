#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#prints all nums except nums ending 0 and 5
for i in range(1, 101):
    if i % 10 == 0 or i % 5 == 0:
        continue
    print(f"{PINK}",i, end=" ")