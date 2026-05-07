user_input = input("Enter text: ")
prefix = input("Enter prefix to check: ")

if len(prefix) > len(user_input):
    print(False)
else:
    print(user_input[:len(prefix)] == prefix)