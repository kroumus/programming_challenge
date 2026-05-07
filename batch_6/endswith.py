main_string = input("Enter the text: ")
target_suffix = input("Enter the suffix to check: ")

# Slice the main string from the end based on suffix length
matches_suffix = main_string[-len(target_suffix):] == target_suffix
print("Ends with suffix?:", matches_suffix)