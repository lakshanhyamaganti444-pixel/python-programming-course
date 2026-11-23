student = {
    "name": "Lakshanhya",
    "age": 18,
    "course": "CSE",
    "city": "Vijayawada"
}
print("Original Dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))
student.update({"age": 19})
print("After Update:", student)
student.pop("city")
print("After Pop:", student)