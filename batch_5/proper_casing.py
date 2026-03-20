#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

fullname = input(f"{PINK}Enter your name: ").capitalize()
print(fullname)