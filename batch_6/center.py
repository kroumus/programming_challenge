user_input = input("Enter text: ")
width = int(input("Enter total width: "))

if width <= len(user_input):
    result = user_input
else:
    total_spaces = width - len(user_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    result = ' ' * left_spaces + user_input + ' ' * right_spaces

print(result)