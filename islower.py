#Replica islower()
user_input = input("Enter text: ")
is_all_lower = True
has_letter = False

for char in user_input:
    if char.isalpha():
        has_letter = True
        if not ('a' <= char <= 'z'):
            is_all_lower = False
            break

print(is_all_lower and has_letter)