students = {
    1: {"name": "Ravi", "marks": 85},
    2: {"name": "Priya", "marks": 90},
    3: {"name": "Rahul", "marks": 78}
}
print("Student Details:")
for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])