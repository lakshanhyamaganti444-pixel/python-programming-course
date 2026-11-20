angle1_in_degrees = float(input("Enter first angle in degrees: "))
angle2_in_degrees = float(input("Enter second angle in degrees: "))
angle3_in_degrees = float(input("Enter third angle in degrees: "))

if (angle1_in_degrees > 0 and angle2_in_degrees > 0 and angle3_in_degrees > 0) and (angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")