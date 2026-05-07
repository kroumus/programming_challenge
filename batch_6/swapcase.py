mixed_case_text = input("Enter text to swap case: ")
swapped_result = ""

for character in mixed_case_text:
    if 'A' <= character <= 'Z':
        swapped_result += chr(ord(character) + 32)
    elif 'a' <= character <= 'z':
        swapped_result += chr(ord(character) - 32)
    else:
        swapped_result += character

print("Result:", swapped_result)