#Replicate title() without using the function
user_input = input("Enter text: ")
result = ""
new_word = True

for char in user_input:
    if char == ' ':
        result += char
        new_word = True
    else:
        if new_word:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
            new_word = False
        else:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char

print(result)