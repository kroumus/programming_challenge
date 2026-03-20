#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

complete_statement = input(f"{PINK}Enter Complete Statement: ").split()

count = len(complete_statement)
print(count)