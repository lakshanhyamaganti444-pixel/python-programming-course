try:
    text = input("Enter a number: ")
    number = int(text)
except ValueError:
    print("Error: Please enter a valid integer")
else:
    square = number * number
    print("Square:", square)
finally:
    print("Program finished")