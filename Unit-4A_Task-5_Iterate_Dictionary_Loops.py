subjects = {
    "Python": 90,
    "Java": 85,
    "HTML": 95,
    "CSS": 88
}
print("Subject Names (Keys):")
for key in subjects.keys():
    print(key)
print("Subject Marks (Values):")
for value in subjects.values():
    print(value)
print("Subject and Marks (Items):")
for key, value in subjects.items():
    print(key, ":", value)