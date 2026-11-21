def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
C = 25
result = convert(C)
print("fahrenheit:", result)