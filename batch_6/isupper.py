check_text = input("Enter text to check if it is all uppercase: ")
is_all_uppercase = True

for character in check_text:
    if 'a' <= character <= 'z':
        is_all_uppercase = False
        break

print("Is it all uppercase?:", is_all_uppercase)