#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

full_name = input(f"{PINK}Enter your name: ").swapcase()
print(full_name)