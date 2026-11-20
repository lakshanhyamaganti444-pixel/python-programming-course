n = int(input("Enter N: "))
largest = float(input("Enter a number: "))
for i in range(1, n):
    num = float(input("Enter a number: "))
    if num > largest:
        largest = num
print("Largest number =", largest)