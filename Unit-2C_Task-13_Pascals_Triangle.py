rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    value = 1
    for j in range(1, i + 1):
        print(value, end=" ")
        value = value * (i - j) // j
    print()