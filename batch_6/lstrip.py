text_to_strip = input("Enter text with leading spaces: ")
index = 0

# Loop until we find a character that is NOT a space
while index < len(text_to_strip) and text_to_strip[index] == ' ':
    index += 1

stripped_text = text_to_strip[index:]
print("Result:", stripped_text)