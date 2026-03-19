#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. 
#Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

full_name = input(f"{PINK}Enter your fullname: ").strip()
print(full_name)