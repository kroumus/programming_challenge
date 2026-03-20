#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

fullname = input(f"{PINK}Enter your name: ").replace(" ", "_").lower()
print(fullname)