user_input = input("Enter text with trailing spaces: ")
index = len(user_input) - 1
while index >= 0 and user_input[index] == ' ':
    index -= 1
result = user_input[:index+1]
print(result)