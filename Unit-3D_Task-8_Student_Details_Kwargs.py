def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_details(name="Krishna", maths=90, science=85, english=80)