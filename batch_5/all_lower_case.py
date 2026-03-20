#Prog04: Create a program that ask the user to input their fullname. Print the input in all lower case.
#Example:
#Input: Juan Dela Cruz
#Output: juan dela cruz

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

fullname = input(f"{PINK}Enter your Name: ").lower()
print(fullname)