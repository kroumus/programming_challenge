user_input = input("Enter text: ")
substring = input("Enter substring to count: ")

count = 0
sub_len = len(substring)
if sub_len == 0:
    print(0)
else:
    for i in range(len(user_input) - sub_len + 1):
        if user_input[i:i+sub_len] == substring:
            count += 1
    print(count)