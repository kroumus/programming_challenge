raw_text = input("Enter text to capitalize: ")
capitalized_result = ""

for index in range(len(raw_text)):
    current_char = raw_text[index]
    if index == 0:
        # Uppercase the first letter
        if 'a' <= current_char <= 'z':
            capitalized_result += chr(ord(current_char) - 32)
        else:
            capitalized_result += current_char
    else:
        # Lowercase everything else
        if 'A' <= current_char <= 'Z':
            capitalized_result += chr(ord(current_char) + 32)
        else:
            capitalized_result += current_char

print("Result:", capitalized_result)