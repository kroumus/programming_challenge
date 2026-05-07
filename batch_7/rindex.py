user_input = input("Enter text: ")
substring = input("Enter substring to find: ")

sub_len = len(substring)
if sub_len == 0:
    print(len(user_input))
else:
    found_index = -1
    for i in range(len(user_input) - sub_len, -1, -1):
        if user_input[i:i+sub_len] == substring:
            found_index = i
            break
    if found_index != -1:
        print(found_index)
    else:
        raise ValueError(f"substring not found")