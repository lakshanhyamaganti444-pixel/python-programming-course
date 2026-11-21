def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter
l = 10
b = 5
a, p = rectangle(l, b)
print("Area:", a)
print("Perimeter:", p)