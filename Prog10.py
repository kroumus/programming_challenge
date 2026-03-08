#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero

for i in range(101):
    if i != 0 and i % 10 == 0:
        continue
    print(i, end=" ") 