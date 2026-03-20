#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
#Example:
#Input: Juan Dela Cruz
#Output: 14

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

full_name = input(f"{PINK}Enter your name: ")
count = len(full_name)
print(count)
