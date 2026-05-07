input_text = input("Enter text to convert to lowercase: ")
lowercase_result = ""

for character in input_text:

    if 'A' <= character <= 'Z':
        lowercase_result += chr(ord(character) + 32)
    else:
        lowercase_result += character

print("Result:", lowercase_result)