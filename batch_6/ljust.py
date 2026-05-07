base_text = input("Enter text: ")
target_width = int(input("Enter total character width: "))

needed_spaces = target_width - len(base_text)

if needed_spaces > 0:
    padded_text = base_text + (' ' * needed_spaces)
else:
    padded_text = base_text

print("Result: '" + padded_text + "'")