user_input = input("Enter text: ")
suffix = input("Enter suffix to remove: ")

if len(suffix) <= len(user_input) and user_input[-len(suffix):] == suffix:
    result = user_input[:-len(suffix)]
else:
    result = user_input

print(result)