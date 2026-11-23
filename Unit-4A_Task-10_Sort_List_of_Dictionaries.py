students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Priya", "marks": 95},
    {"name": "Rahul", "marks": 75}
]
ascending = sorted(students, key=lambda x: x["marks"])
print("Ascending Order:")
print(ascending)
descending = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Descending Order:")
print(descending)