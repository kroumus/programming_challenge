#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

fullname = input(f"{PINK}Enter your name: ").title().replace(" ", "")
print(fullname)