user_input = input("Enter text: ")
width = int(input("Enter total width: "))

if width <= len(user_input):
    result = user_input
else:
    result = ' ' * (width - len(user_input)) + user_input

print(result)
print(f"Length: {len(result)}")