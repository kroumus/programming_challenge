#Prog02: Create a program that ask the user to input a number (0-1000). 
#Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143

#make it color pink daw sabi ng bebi ko
PINK = '\033[38;2;255;182;193m'

#ask the user to input a number (0-1000)
numbers = int(input(f"{PINK}Enter Number (0-1000): "))


if numbers < 0 or numbers > 1000:
    print("Invalid")
elif numbers >= 0 or numbers <= 9:
    print( print(f"00000{numbers}"))
elif numbers == 1000:
    print(f"00{numbers}")
else:
    print(f"000{numbers}")
