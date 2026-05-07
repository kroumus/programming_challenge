user_input = input("Enter text (number): ")
width = int(input("Enter total width: "))

if width <= len(user_input):
    result = user_input
else:
    if user_input.startswith('-'):
        result = '-' + '0' * (width - len(user_input)) + user_input[1:]
    else:
        result = '0' * (width - len(user_input)) + user_input

print(result)