s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", "")):
    print("Anagram")
else:
    print("Not Anagram")